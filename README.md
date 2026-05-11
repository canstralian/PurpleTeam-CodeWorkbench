---
title: Purple Team Code Workbench
emoji: 👀
colorFrom: purple
colorTo: indigo
sdk: streamlit
sdk_version: 1.57.0
python_version: '3.11'
app_file: app.py
pinned: true
license: apache-2.0
short_description: |
  AI workbench for purple-team security workflows.
tags:
- cybersecurity
- purple-team
- defensive-security
- ai-security
- code-generation
- streamlit
- llm
- red-team
- blue-team
- security-research
- transformers
- generative-ai
models:
- DeepHat/DeepHat-V1-7B
- HauhauCS/Gemma-4-E4B-Uncensored-HauhauCS-Aggressive
- meta-llama/Meta-Llama-3-8B-Instruct
suggested_hardware: cpu-upgrade
suggested_storage: small
thumbnail: >-
  https://cdn-uploads.huggingface.co/production/uploads/67c714e90b99a2332e310979/L02-prFfHa7eBZGVf4uvR.jpeg
---

# Purple Team Code Workbench

<p align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/67c714e90b99a2332e310979/L02-prFfHa7eBZGVf4uvR.jpeg" width="720" alt="Purple Team Code Workbench Banner"/>
</p>
<p align="center">
  <strong>Streamlit-powered code generation and workflow orchestration surface for authorized purple-team operations.</strong>
</p>
<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/python-3.11%2B-blue">
  <img alt="Streamlit" src="https://img.shields.io/badge/streamlit-1.57.0-red">
  <img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-green">
  <img alt="Security" src="https://img.shields.io/badge/focus-purple--team-purple">
</p>

⸻

## Overview

Purple Team Code Workbench is an AI-assisted cybersecurity experimentation environment designed for defensive researchers, purple-team operators, and security engineers. The platform combines LLM-driven code generation, workflow prototyping, and adversarial simulation capabilities inside a lightweight Streamlit interface.

The platform focuses on:

- Authorized assessment workflows
- Defensive and adversarial simulation support
- Code generation for security operations
- Evidence handling and finding management
- Prompt-assisted workflow acceleration
- Report artifact generation
- Research and analysis augmentation

The system is intentionally structured around controlled workflows rather than unrestricted autonomous execution. Because the internet already contains enough entropy generators wearing hoodies and calling themselves “operators.”

---

## Safety & Intended Use

Purple Team Code Workbench is intended for:

- Authorized security testing
- Defensive security research
- Secure software experimentation
- Educational cybersecurity workflows
- Purple-team simulation and analysis

This project is not intended for unauthorized access, malware deployment, credential theft, persistence mechanisms, or destructive operations.

Users are responsible for complying with applicable laws, organizational policies, and authorization requirements.

---

## Model Roles

| Model | Purpose |
|---|---|
| Gemma-4-E4B-Uncensored | Creative adversarial ideation and unrestricted experimentation |
| DeepHat-V1-7B | Security-oriented coding and workflow assistance |
| Llama 3 8B Instruct | General reasoning and structured instruction following |

---

## Runtime Environment

- Python 3.11
- Streamlit 1.57.0
- Transformers-based inference stack
- CPU-compatible deployment
- Optional GPU acceleration

---

## Core Design Principles

### Scope-First Architecture

Every workflow begins with explicit authorization and target definition.

The system is designed to reduce:

- accidental scope drift
- unsafe automation
- uncontrolled execution paths
- ambiguous operational state

---

### Human-in-the-Loop Control

The workbench assists analysts and engineers rather than replacing operational judgment.

Generation ≠ execution.

All generated output should be reviewed before use.

---

### Evidence-Centric Workflow

Outputs are treated as operational artifacts:

- findings
- prompts
- code snippets
- reports
- remediation notes
- validation records

The system emphasizes traceability and reproducibility over “magic AI behavior.”

A tragically rare design choice in 2026.

---

## Features

### Current Capabilities

- Streamlit-based UI
- Scope-gated workflow controls
- Security code generation surface
- Passive recon helpers
- Structured findings management
- Markdown report export
- Multi-model workflow support
- Hugging Face Space deployment compatibility

---

### Planned Capabilities

- Agent orchestration
- Prompt chaining
- Workflow templates
- Typed finding schemas
- Evidence graphing
- Drift-aware execution state
- Multi-provider inference routing
- Report diff/version tracking
- Local LLM runtime support
- LangGraph integration
- MCP-compatible tool surfaces

---

## Supported Models

Current configured models:

| Model | Purpose |
|---|---|
| HauhauCS/Gemma-4-E4B-Uncensored-HauhauCS-Aggressive | Experimental coding and reasoning |
| DeepHat/DeepHat-V1-7B | Security-oriented generation workflows |
| llama3-8b-8192 | General-purpose assistant workflows |

Model availability depends on provider access and deployment configuration.

---

## Repository Structure

text . ├── app.py ├── requirements.txt ├── README.md ├── assets/ ├── workflows/ ├── prompts/ ├── reports/ ├── utils/ └── components/ 

Recommended modularization:

| Directory | Purpose |
|---|---|
| workflows/ | Workflow orchestration logic |
| prompts/ | Prompt templates and chains |
| reports/ | Generated report artifacts |
| utils/ | Shared utilities |
| components/ | Streamlit UI components |
| assets/ | Static images and branding |

---

## Installation

### Local Development

Clone the repository:

bash git clone https://github.com/your-org/purple-team-code-workbench.git cd purple-team-code-workbench 

Create a virtual environment:

bash python -m venv .venv 

Activate the environment:

#### Linux/macOS

bash source .venv/bin/activate 

#### Windows

powershell .venv\Scripts\activate 

Install dependencies:

bash pip install -r requirements.txt 

Run the application:

bash streamlit run app.py 

---

## Hugging Face Spaces Deployment

This repository is compatible with:

- Hugging Face Streamlit Spaces
- CPU deployments
- OAuth-enabled Spaces
- External inference providers

Example metadata:

yaml sdk: streamlit sdk_version: 1.57.0 app_file: app.py license: apache-2.0 

---

## Security Philosophy

This project is intended for:

- authorized testing
- defensive research
- purple-team simulation
- workflow engineering
- educational environments
- internal security operations

This repository is not intended for:

- unauthorized access
- destructive automation
- malware deployment
- credential theft
- persistence tooling
- uncontrolled exploitation

Users are responsible for complying with all applicable laws and authorization requirements.

Tiny administrative detail. Society gets strangely emotional about “cybercrime.”

---

## Recommended Operational Controls

If deploying in production environments:

- Require authentication
- Log workflow activity
- Separate trusted/untrusted prompts
- Sandbox execution environments
- Restrict outbound networking
- Validate generated artifacts
- Maintain immutable audit trails
- Enforce scoped execution policies

---

## Example Workflow

text Scope Definition     ↓ Passive Recon     ↓ Evidence Collection     ↓ Finding Classification     ↓ Code/Prompt Generation     ↓ Human Validation     ↓ Report Export 

---

## Development Roadmap

### Phase 1
- Scope-gated workflows
- Findings management
- Report export
- Prompt surface

### Phase 2
- Agent coordination
- Structured memory
- Typed contracts
- Multi-model routing

### Phase 3
- Drift-aware orchestration
- Evidence graphs
- Policy enforcement engine
- Autonomous validation loops

---

## Contributing

Contributions should prioritize:

- clarity
- safety
- reproducibility
- deterministic behavior
- typed interfaces
- operational traceability

Before submitting:

- run linting
- validate workflows
- document assumptions
- avoid opaque automation behavior

---

## License

Licensed under the Apache 2.0 License.

See the LICENSE file for details.

---

## Disclaimer

This project is provided for authorized security research, defensive engineering, and educational purposes only.

The maintainers assume no liability for misuse, unauthorized deployment, or operational damage caused by derivative implementations.

Generated outputs may contain inaccuracies, insecure assumptions, or incomplete implementations. Human review is required before production or operational use.

---

## Acknowledgements

Built with:

- Streamlit
- Hugging Face
- Python Software Foundation

Inspired by structured operational engineering, purple-team methodology, and the stubborn belief that security tooling should behave like systems engineering rather than ritual magic.