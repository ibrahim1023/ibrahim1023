# Ibrahim Arshad

Blockchain Infrastructure Engineer focused on protocol engineering, verification-oriented tooling, and Rust systems work across Ethereum, Solana, Sui, and Stellar, with active AI engineering work in reliability and agentic systems.

I build infrastructure and workflows for protocol correctness and production AI reliability: smart contract invariants, assumption tracking, audit readiness, reproducible verification evidence, and evidence-first AI system evaluation.

Core stack: Rust, Solidity, Move, Python.

---

## Current Focus

- Building [ProofBoard](https://github.com/ibrahim1023/ProofBoard)
- Contributing to `paradigmxyz/reth`
- Contributing to `alloy-rs/alloy`
- Exploring protocol verification workflows
- Smart contract correctness and invariant-driven development
- Multi-chain infrastructure across Ethereum, Solana, Sui, and Stellar
- zkVM and proof-system research

---

## Open Source Contributions

### Recent Open Source Work

Auto-fetched open and merged PRs across external projects:

<!-- PRS:START -->

- [Merged] [#2331](https://github.com/langchain-ai/langgraphjs/pull/2331) fix(langgraph): handle null thread checkpoint in RemoteGraph.getState in `langchain-ai/langgraphjs`
- [Open] [#21336](https://github.com/run-llama/llama_index/pull/21336) fix(elasticsearch): split sync and async store paths in `run-llama/llama_index`
- [Open] [#3996](https://github.com/alloy-rs/alloy/pull/3996) fix(provider): poll receipts while waiting for confirmations in `alloy-rs/alloy`
- [Open] [#24337](https://github.com/paradigmxyz/reth/pull/24337) fix(download): avoid checksum scan during resume startup in `paradigmxyz/reth`
- [Open] [#8957](https://github.com/qdrant/qdrant/pull/8957) Fix 8935 match except dev in `qdrant/qdrant`
- [Open] [#6535](https://github.com/graphprotocol/graph-node/pull/6535) fix(ethereum): handle trace_filter traces missing result.output via c… in `graphprotocol/graph-node`
- [Open] [#5461](https://github.com/crewAIInc/crewAI/pull/5461) fix(converter): fall back on invalid JSON-like partial matches in `crewAIInc/crewAI`
- [Open] [#21386](https://github.com/run-llama/llama_index/pull/21386) fix(azureaisearch): preserve falsy metadata values in index mapping in `run-llama/llama_index`
- [Merged] [#39169](https://github.com/vllm-project/vllm/pull/39169) fix(gdn): Align prefill warmup with real prefill path in `vllm-project/vllm`
- [Open] [#10](https://github.com/logos-co/logos-lez-rln/pull/10) Fix #9: update guest code for current `nssa_core` program API in `logos-co/logos-lez-rln`

<!-- PRS:END -->

### Blockchain Infrastructure

- `paradigmxyz/reth`: improved archive download resume startup by removing heavy checksum scanning before progress begins ([#24337](https://github.com/paradigmxyz/reth/pull/24337)).
- `alloy-rs/alloy`: fixed confirmation wait flow so pending transaction receipt polling continues reliably ([#3996](https://github.com/alloy-rs/alloy/pull/3996)).

### AI Infrastructure

- `langchain-ai/langgraphjs`: fixed remote graph state handling for null checkpoints ([#2331](https://github.com/langchain-ai/langgraphjs/pull/2331)).
- `vllm-project/vllm`: aligned prefill warmup path with real prefill execution behavior ([#39169](https://github.com/vllm-project/vllm/pull/39169)).
- `crewAIInc/crewAI`: improved structured output parsing fallback for invalid JSON-like partial matches ([#5461](https://github.com/crewAIInc/crewAI/pull/5461)).

---

## Featured Projects

### 1) [ProofBoard](https://github.com/ibrahim1023/ProofBoard)

ProofBoard is a protocol correctness workspace for smart contracts.

Problem: many protocol failures come from mismatched assumptions, unstated invariants, and weak verification workflows rather than obvious syntax bugs. Traditional audits are necessary but point-in-time, and they do not always encode evolving protocol intent as executable checks.

ProofBoard turns protocol intent into testable artifacts:

- explicit protocol assumptions
- executable invariants
- verification workflows tied to those invariants
- evidence ledgers for verification runs
- audit-readiness packets for review and handoff

Why this matters in DeFi:

- protocol safety depends on behavior under adversarial conditions
- correctness requires continuous validation, not one-time review
- teams need traceable evidence connecting intent to test outcomes

Long-term vision: make verification-oriented protocol development the default workflow from design to deployment.

### 2) [ci-rootcause](https://github.com/ibrahim1023/ci-rootcause)

Deterministic CI failure investigation for GitHub Actions with evidence-first RCA artifacts, guarded fix generation, and reproducible validation loops.

### 3) AI Reliability Tooling

Evaluation-oriented AI engineering work focused on deterministic workflows, guarded automation, and reproducible validation for agent-assisted systems.

---

## Technical Writing

### AI Systems and Reliability

- [AI Coding Agents Need Evidence, Not Confidence](https://medium.com/@ibrahim.a.motiwala/ai-coding-agents-need-evidence-not-confidence-7b398a48a0ec)
- [CI Failures Are Not Text Problems. They Are Execution Problems.](https://medium.com/p/e8ab5db074cd)

Planned writing themes:

- evaluation-first AI engineering
- deterministic agent workflows
- CI reliability and evidence-backed RCA
- guardrails and validation in AI-assisted development

---

## Skills and Interests

### Blockchain

- Rust
- Solidity
- Move
- Stellar
- Ethereum
- Solana
- Sui

### Protocols

- Lending protocols
- DEX infrastructure
- Governance systems
- Vault architectures
- Smart contract security

### Infrastructure

- Reth
- Alloy
- RPC systems
- Blockchain indexing
- Distributed systems
- Observability

### AI

- LangGraph
- LangChain
- vLLM
- Agent systems
- AI reliability

---

## Research Interests

- Protocol correctness
- Verification-oriented development
- Smart contract security
- Ethereum infrastructure
- zkVMs
- Formal verification
- Distributed systems
- AI reliability

---

## Contact

- [GitHub](https://github.com/ibrahim1023)
- [LinkedIn](https://www.linkedin.com/in/ibrahim-arshad-23355a166/)
- [Medium](https://medium.com/@ibrahim.a.motiwala)
