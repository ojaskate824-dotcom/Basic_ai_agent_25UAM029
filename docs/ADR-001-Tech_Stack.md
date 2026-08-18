# ADR 1: Selection of Tech Stack for Basic AI Agent

## Status
Accepted

## Context
As part of the "AI-Augmented Workflow" course, we need to design a basic AI Agent for an e-Portfolio project. To prioritize privacy, eliminate API cost risks, and remove credential/key management from the codebase, we require an entirely local development environment. 

## Decision
We will use **Python 3.11+**, **Ollama** (running the `llama3.2:1b` model) as our local reasoning engine, and the **OpenAI Python SDK** directed to a localhost server wrapper. Development will be enhanced using **GitHub Copilot** inside **VS Code**, utilizing **Git Bash** as the primary CLI tool.

## Consequences

### Pros
* **Zero Cost & No Keys:** No OpenAI accounts or API keys are required, eliminating credential leak risks.
* **100% Offline Capability:** The entire stack runs locally on the machine without network requests.
* **High AI-Assisted Synergy:** GitHub Copilot seamlessly auto-completes Python commands and Ollama configurations due to high training data density.

### Cons
* **Local Compute Dependency:** Performance relies completely on local CPU/GPU hardware.
* **Smaller Model Constraints:** The 1-billion parameter model may offer less complex reasoning than massive cloud models like GPT-4.
