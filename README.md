# 👋 Hi, I’m Ibrahim

I’m a software engineer focused on **deterministic systems, AI reliability, and production-grade GenAI tooling**.

I like building things that reduce ambiguity: explicit workflows, clear contracts, reproducible runs, and systems that are easy to reason about and debug.

---

## 🚧 Current Projects

### llmdiff — LLM Diff & Regression Testing Framework
**Status:** In progress

Snapshot + contract testing for LLM systems with semantic diffing and CI regression gates.

Production-grade regression testing for LLM systems.
- Snapshot + contract testing for prompts
- Semantic diffing (LLM-as-judge)
- Tool-call validation
- Cost & latency regression tracking
- CI-ready exit codes

Designed to bring reproducibility and guardrails to nondeterministic LLM pipelines.

### llmflow-core — Deterministic LLM Workflow Engine  
**Status:** Active (Published on PyPI)

A **library-first, deterministic workflow engine** for running LLM-powered pipelines as explicit, human-readable steps — without autonomous agents.

LLMFlow enforces:
- Explicit DAG-based execution order
- Schema-validated LLM outputs (fail-fast)
- Prompt files as versioned artifacts
- Replayable runs with stored metadata
- Deterministic configuration (temperature control)

Designed to plug into existing AI applications where predictability,
auditability, and control matter more than autonomy.

📦 [PyPI](https://pypi.org/project/llmflow-core/)   
🔗 [Repo](https://github.com/ibrahim1023/llmflow-core) 

---

## 🧪 Learning Projects

The following projects were built to **explore and stress-test ideas** around AI workflows,
determinism, and reasoning systems.

---

### [Multi-Source RAG System](https://github.com/ibrahim1023/multi-source-rag-system)  

An implementation of a retrieval-augmented generation system that aggregates results from
multiple data sources before generation.

- Focus: RAG architecture, grounding, and retrieval composition
- Explored trade-offs between single-source vs multi-source retrieval
- Helped build intuition for reliability issues in RAG pipelines
---

### [Prompt Playground](https://github.com/ibrahim1023/prompt-playground)  

A structured playground for experimenting with **prompt engineering techniques** and
understanding how prompt changes affect model behavior.

- Focus: prompt iteration, structure, and constraints
- Emphasis on reproducibility and clarity over ad-hoc prompting
- Reinforced the importance of treating prompts as versioned artifacts
---

### [Deterministic Multi-Step Reasoning Engine](https://github.com/ibrahim1023/deterministic-multi-step-engine)  

A prototype engine exploring **deterministic step execution**, explicit control flow, and
state propagation across multi-step reasoning pipelines.

- Focus: deterministic execution and step orchestration
- Highlighted limitations of generic step engines for LLM workflows
- Directly informed the design philosophy behind `llmflow-core`
---

## 🎯 Current Interests

- Deterministic and auditable AI systems
- LLM reliability, validation, and evaluation
- AI developer tooling & infrastructure
- Production-grade GenAI architectures

---

## 📫 Get in touch

- [GitHub](https://github.com/ibrahim1023)
- [LinkedIn](https://www.linkedin.com/in/ibrahim-arshad-23355a166/)
