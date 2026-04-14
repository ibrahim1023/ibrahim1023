#!/usr/bin/env python3
"""
Update a README section with the latest open and merged pull requests.

Expected markers in the README:
<!-- PRS:START -->
... generated content ...
<!-- PRS:END -->
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone


START_MARKER = "<!-- PRS:START -->"
END_MARKER = "<!-- PRS:END -->"
GITHUB_API_BASE = "https://api.github.com"
DEFAULT_USER = "ibrahim1023"
DEFAULT_LIMIT = 5
ENV_FILE = ".env"


@dataclass
class PullRequest:
    number: int
    title: str
    url: str
    author: str
    repository: str
    state: str
    updated_at: str
    merged_at: str | None = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Update a README section with latest GitHub pull requests."
    )
    parser.add_argument(
        "--user",
        default=DEFAULT_USER,
        help="GitHub username whose authored PRs should be listed.",
    )
    parser.add_argument(
        "--readme",
        default="README.md",
        help="Path to the README file to update.",
    )
    parser.add_argument(
        "--open-limit",
        type=int,
        default=DEFAULT_LIMIT,
        help="Number of open PRs to include.",
    )
    parser.add_argument(
        "--merged-limit",
        type=int,
        default=DEFAULT_LIMIT,
        help="Number of merged PRs to include.",
    )
    return parser.parse_args()


def load_dotenv(path: str = ENV_FILE) -> None:
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for raw_line in fh:
                line = raw_line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue

                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip().strip("'\"")
                if key:
                    os.environ.setdefault(key, value)
    except FileNotFoundError:
        return


def get_github_token() -> str | None:
    token = os.getenv("GITHUB_TOKEN")
    if token:
        return token.strip()

    try:
        result = subprocess.run(
            ["gh", "auth", "token"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None

    token = result.stdout.strip()
    return token or None


def github_get(
    path: str,
    token: str | None,
    query: dict[str, str | int] | None = None,
) -> list[dict] | dict:
    url = f"{GITHUB_API_BASE}{path}"
    if query:
        url = f"{url}?{urllib.parse.urlencode(query)}"

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "readme-pr-updater",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(request) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"GitHub API request failed ({exc.code}): {body}") from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"Could not reach GitHub API: {exc}") from exc


def fetch_search_prs(
    user: str,
    state_filter: str,
    limit: int,
    token: str | None,
) -> list[PullRequest]:
    state_label = "Merged" if state_filter == "is:merged" else "Open"
    response = github_get(
        "/search/issues",
        token,
        query={
            "q": f"type:pr author:{user} {state_filter} sort:updated-desc",
            "sort": "updated",
            "order": "desc",
            "per_page": limit,
        },
    )
    items = response.get("items", [])
    return [
        PullRequest(
            number=pr["number"],
            title=pr["title"],
            url=pr["html_url"],
            author=pr["user"]["login"],
            repository=pr["repository_url"].removeprefix(f"{GITHUB_API_BASE}/repos/"),
            state=state_label,
            updated_at=pr["updated_at"],
            merged_at=pr.get("closed_at") if state_filter == "is:merged" else None,
        )
        for pr in items
    ]


def fetch_open_prs(user: str, limit: int, token: str | None) -> list[PullRequest]:
    return fetch_search_prs(user, "is:open", limit, token)


def fetch_merged_prs(user: str, limit: int, token: str | None) -> list[PullRequest]:
    return fetch_search_prs(user, "is:merged", limit, token)


def parse_github_timestamp(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def render_section(
    open_prs: list[PullRequest],
    merged_prs: list[PullRequest],
    user: str,
) -> str:
    prs = sorted(
        [*open_prs, *merged_prs],
        key=lambda pr: parse_github_timestamp(pr.updated_at),
        reverse=True,
    )[:DEFAULT_LIMIT]
    lines = [
        START_MARKER,
        f"[github.com/{user}](https://github.com/{user})",
    ]

    if prs:
        lines.append("")
        lines.extend(
            f"- [{pr.state}] [#{pr.number}]({pr.url}) {pr.title} in `{pr.repository}`"
            for pr in prs
        )
    else:
        lines.extend(["", "- No pull requests found."])

    lines.extend(["", END_MARKER])
    return "\n".join(lines)


def replace_marked_section(readme_text: str, new_section: str) -> str:
    if START_MARKER not in readme_text or END_MARKER not in readme_text:
        raise SystemExit(
            f"README must contain both markers: {START_MARKER} and {END_MARKER}"
        )

    start = readme_text.index(START_MARKER)
    end = readme_text.index(END_MARKER) + len(END_MARKER)
    return f"{readme_text[:start]}{new_section}{readme_text[end:]}"


def main() -> None:
    args = parse_args()
    load_dotenv()
    token = get_github_token()

    try:
        with open(args.readme, "r", encoding="utf-8") as fh:
            readme_text = fh.read()
    except FileNotFoundError as exc:
        raise SystemExit(f"README not found: {args.readme}") from exc

    open_prs = fetch_open_prs(args.user, args.open_limit, token)
    merged_prs = fetch_merged_prs(args.user, args.merged_limit, token)
    new_section = render_section(open_prs, merged_prs, args.user)
    updated = replace_marked_section(readme_text, new_section)

    with open(args.readme, "w", encoding="utf-8") as fh:
        fh.write(updated)

    print(
        f"Updated {args.readme} with {len(open_prs)} open PR(s) and {len(merged_prs)} merged PR(s)."
    )


if __name__ == "__main__":
    main()
