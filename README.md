# Ibrahim Arshad

Building deterministic AI systems, not demos.

---

## About

Software engineer focused on agentic AI systems and blockchain.

I build:
- multi-agent systems with structured orchestration  
- deterministic harnesses for reliability  
- evaluation-aware AI systems (focused on correctness, not just output)

Focus areas:
- agent orchestration (LangChain, LangGraph, custom harnesses)
- context + tool design (ACI-style systems)
- AI evaluation (failure detection, reproducibility, ranking)
- Blockchain development

### Currently working across
→ AI systems (LLM workflows, agent orchestration, evaluation)  
→ Distributed systems + automation tooling  

---
## Featured Project: [ci-rootcause](https://github.com/ibrahim1023/ci-rootcause)

Deterministic multi-agent CI debugging engine.

Most AI CI tools summarize logs.  
They fail because CI failures are execution systems, not text problems.

ci-rootcause reconstructs execution and identifies the actual root cause.

### What it does

- builds a failure graph from CI logs  
- detects the first failure (not downstream symptoms)  
- analyzes diffs to link code changes to breakages  
- ranks root causes using deterministic scoring  
- generates evidence-backed fixes (LLM-constrained)  
- produces structured outputs: `ci-rca.json`, `ci-rca.md`

### LLM Support (Pluggable)

LLMs are used selectively for:
- explanation  
- fix suggestions  

Supported providers:
- Ollama (local models)
- OpenAI
- Anthropic
- Google Gemini

LLMs are never used for scoring or confidence.

### Why it matters

- no hallucinated root causes  
- reproducible outputs across runs  
- confidence is computed, not generated  
- works with both local and hosted models  
- designed for real CI workflows, not demos  

### Core Principles

- determinism over heuristics  
- systems over prompts  
- evaluation before optimization  
- evidence over plausibility

### Output

- `ci-rca.json` → machine-readable root cause  
- `ci-rca.md` → human-readable explanation  
---

## Open Source Focus (2026)

- contributing to real AI systems (not toy projects)
- building production-grade agent workflows
- focusing on correctness, determinism, and evaluation
- shipping systems that can be reasoned about and verified

Approach:
→ consistent, high-frequency contributions
→ focus on real issues that get merged  

### PRs

<!-- PRS:START -->

- [Open] [#8957](https://github.com/qdrant/qdrant/pull/8957) Fix 8935 match except dev in `qdrant/qdrant`
- [Open] [#6535](https://github.com/graphprotocol/graph-node/pull/6535) fix(ethereum): handle trace_filter traces missing result.output via c… in `graphprotocol/graph-node`
- [Merged] [#4](https://github.com/ibrahim1023/ci-rootcause/pull/4) test: trigger failing workflow_run for app smoke in `ibrahim1023/ci-rootcause`
- [Open] [#2331](https://github.com/langchain-ai/langgraphjs/pull/2331) fix(langgraph): handle null thread checkpoint in RemoteGraph.getState in `langchain-ai/langgraphjs`
- [Open] [#5461](https://github.com/crewAIInc/crewAI/pull/5461) fix(converter): fall back on invalid JSON-like partial matches in `crewAIInc/crewAI`
- [Open] [#2316](https://github.com/langchain-ai/langgraphjs/pull/2316) fix(sdk): Backfill truncated history for regenerate branching in `langchain-ai/langgraphjs`
- [Open] [#21386](https://github.com/run-llama/llama_index/pull/21386) fix(azureaisearch): preserve falsy metadata values in index mapping in `run-llama/llama_index`

<!-- PRS:END -->

## Engineering Principles

- Determinism over heuristics where possible  
- Systems over prompts  
- Evaluation before optimization  
- Evidence > plausibility

---

## Skills

### AI Systems
- LangChain  
- LangGraph  
- multi-agent orchestration  
- LLM tool + context design

### Blockchain
- EVM
- Smart Contracts
- DeFi Infrastructure
- Blockchain Indexing
- RPC Systems
- Event Processing
- Transaction Validation

### Infrastructure / Systems
- Python  
- TypeScript  
- Rust  

### Focus Areas
- agent harness design  
- evaluation systems  
- reproducibility + reliability  

---

## Contact

- [GitHub](https://github.com/ibrahim1023) 
- [LinkedIn](https://www.linkedin.com/in/ibrahim-arshad-23355a166/)
