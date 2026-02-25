# 👋 Hi, I’m Ibrahim

I’m a software engineer focused on **deterministic systems, AI reliability, and production-grade GenAI tooling**.

I like building things that reduce ambiguity: explicit workflows, clear contracts, reproducible runs, and systems that are easy to reason about and debug.

---

## 🚧 Current Projects

#### screenflow-ios — On-Screen Understanding → AI Action Engine (iOS)
screenflow-ios is an AI-powered iOS app that converts screenshots into structured, actionable workflows. It analyzes on-screen content, extracts meaningful context, and uses LLMs to generate relevant actions users can execute instantly. The system combines visual parsing, semantic understanding, and a modular action engine to turn passive screen content into useful outcomes.

#### [ci-rootcause](https://github.com/ibrahim1023/ci-rootcause) — Multi-Agent CI Debugging Engine [In progress]
An ADK-oriented multi-agent CI analysis system that deterministically extracts first failure, builds failure graphs, correlates failures with diffs, ranks root causes with computed confidence (not LLM-generated), proposes evidence-grounded fixes, and can open a guarded fix PR (never auto-merged). Produces ci-rca.json and ci-rca.md artifacts.

#### [llmflow-core](https://github.com/ibrahim1023/llmflow-core) — Deterministic LLM Workflow Engine
A production-ready SDK for building deterministic, multi-step LLM workflows with strict execution guarantees and structured reasoning.
Focused on reliability, reproducibility, and eliminating hallucination-prone agent loops.

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
