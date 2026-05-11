---
title: Purple Team Code Workbench

emoji: 🛠️

colorFrom: purple
colorTo: indigo

sdk: streamlit
sdk_version: 1.57.0

python_version: "3.11"

app_file: app.py

pinned: true

license: apache-2.0

short_description: AI workbench for purple-team security workflows.

tags:
  - cybersecurity
  - purple-team
  - defensive-security
  - ai-security
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
  <strong>
    Streamlit-powered code generation and workflow orchestration
    surface for authorized purple-team operations.
  </strong>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/python-3.11%2B-blue">
  <img alt="Streamlit" src="https://img.shields.io/badge/streamlit-1.57.0-red">
  <img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-green">
  <img alt="Security" src="https://img.shields.io/badge/focus-purple--team-purple">
</p>

---

## Overview

Purple Team Code Workbench is an AI-assisted cybersecurity experimentation environment designed for defensive researchers, purple-team operators, and security engineers.

The platform combines:

- LLM-driven code generation
- Workflow prototyping
- Adversarial simulation
- Structured findings management
- Report generation
- Human-in-the-loop operational control

inside a lightweight Streamlit interface.

This repository currently includes a working starter implementation with a scope gate, workflow prompt builder, structured findings manager, hash-linked evidence ledger, model profile panel, and Markdown report export. It is designed to run locally or as a Hugging Face Streamlit Space without requiring a GPU.

The architecture emphasizes modular orchestration, reproducible workflows, and human-supervised operational control.

The platform focuses on:

- Authorized assessment workflows
- Defensive and adversarial simulation support
- Code generation for security operations
- Evidence handling and finding management
- Prompt-assisted workflow acceleration
- Report artifact generation
- Research and analysis augmentation

The system is intentionally structured around controlled workflows rather than unrestricted autonomous execution.

---

## Why Purple Team?

Purple-team methodology combines offensive security simulation with defensive validation and detection engineering.

This workbench is designed to support collaborative workflows between:

- security researchers
- defenders
- detection engineers
- SOC analysts
- incident responders
- application security teams

The focus is operational learning, validation, and resilience improvement rather than isolated offensive capability.

---

## Safety & Intended Use

Purple Team Code Workbench is intended for:

- Authorized security testing
- Defensive security research
- Secure software experimentation
- Educational cybersecurity workflows
- Purple-team simulation and analysis

This project is not intended for:

- Unauthorized access
- Malware deployment
- Credential theft
- Persistence mechanisms
- Destructive operations
- Autonomous offensive activity

Users are responsible for complying with applicable laws, organizational policies, and authorization requirements.

---

## Non-Goals

This project is not intended to provide:

- autonomous offensive operations
- malware automation
- persistence tooling
- uncontrolled exploitation workflows
- credential harvesting systems

---

## Model Roles

| Model | Purpose |
|---|---|
| HauhauCS/Gemma-4-E4B-Uncensored-HauhauCS-Aggressive | Experimental reasoning and adversarial simulation support |
| DeepHat/DeepHat-V1-7B | Security-oriented coding and workflow assistance |
| meta-llama/Meta-Llama-3-8B-Instruct | General reasoning and structured instruction following |

---

## Runtime Environment

- Python 3.11
- Streamlit 1.57.0
- pandas
- CPU-compatible deployment
- Optional GPU acceleration if model inference is added later
- Hugging Face Streamlit Space compatibility

The included starter app is intentionally lightweight. It can run locally or inside a Hugging Face Space without requiring a GPU.

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

The system emphasizes traceability and reproducibility over opaque AI behavior.

A tragically rare design choice in modern software tooling.

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
- CPU-compatible starter runtime
- Session-state based local workflow records
- JSON, CSV, and Markdown exports

---

### Included Starter Files

The current starter package contains:

| File | Purpose |
|---|---|
| `app.py` | Main Streamlit application |
| `requirements.txt` | Python dependencies |
| `README.md` | Hugging Face Space metadata and project documentation |
| `.streamlit/config.toml` | Theme and server defaults |

The app does **not** call external model APIs by default. The configured model list is used as a profile/routing layer so inference can be added later without hiding provider behavior inside the UI. Because invisible API calls are how dashboards become haunted.

---

### Planned Capabilities

- Workflow templates
- Prompt chaining
- Agent orchestration
- Typed finding schemas
- Multi-provider inference routing
- Local LLM runtime support
- Evidence graphing
- Drift-aware execution state
- Report diff/version tracking
- LangGraph integration
- MCP-compatible tool surfaces

---

## Supported Models

Current configured models:

| Model | Purpose |
|---|---|
| HauhauCS/Gemma-4-E4B-Uncensored-HauhauCS-Aggressive | Experimental coding and reasoning |
| DeepHat/DeepHat-V1-7B | Security-oriented generation workflows |
| Meta-Llama-3-8B-Instruct | General-purpose assistant workflows |

Model availability depends on provider access and deployment configuration.

---

## Repository Structure

Current starter package:

```text
.
├── app.py
├── requirements.txt
├── README.md
└── .streamlit/
    └── config.toml
```

Recommended expanded structure:

```text
.
├── app.py
├── requirements.txt
├── README.md
├── assets/
├── workflows/
├── prompts/
├── reports/
├── utils/
├── components/
└── tests/
```

Recommended modularization:

| Directory | Purpose |
|---|---|
| workflows/ | Workflow orchestration logic |
| prompts/ | Prompt templates and chains |
| reports/ | Generated report artifacts |
| utils/ | Shared utilities |
| components/ | Streamlit UI components |
| assets/ | Static images and branding |
| tests/ | Unit tests and workflow validation checks |

---

## Installation

### Local Development

Clone the repository:

```bash
git clone https://github.com/your-org/purple-team-code-workbench.git
cd purple-team-code-workbench
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

#### Linux/macOS

```bash
source .venv/bin/activate
```

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
.venv\Scripts\activate.bat
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Hugging Face Spaces Deployment

This repository is compatible with:

- Hugging Face Streamlit Spaces
- CPU deployments
- OAuth-enabled Spaces
- External inference providers

The README front matter already includes Space metadata:

```yaml
sdk: streamlit
sdk_version: 1.57.0
python_version: "3.11"
app_file: app.py
license: apache-2.0
suggested_hardware: cpu-upgrade
suggested_storage: small
```

Basic deployment path:

1. Create a new Hugging Face Space.
2. Select **Streamlit** as the SDK.
3. Upload `app.py`, `requirements.txt`, `README.md`, and `.streamlit/config.toml`.
4. Confirm the Space builds against Python 3.11 and Streamlit 1.57.0.
5. Add secrets only if external inference providers are integrated later.

---

## Inference Providers

The starter app does not include live inference calls by default.

Future provider integrations may use:

- Hugging Face Inference Providers
- External API routing
- Local runtime configuration
- OAuth authentication state
- Deployment hardware constraints

Recommended provider design:

- keep API keys in environment variables or Space secrets
- separate provider logic from UI components
- log model profile, prompt template, and output metadata
- avoid storing secrets in reports, findings, or exported prompt artifacts
- treat model output as untrusted until reviewed

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
- Require approval before provider calls
- Prevent secrets from entering exported reports
- Separate draft generation from operational action

---

## Example Workflow

```text
Scope Definition
        ↓
Passive Recon
        ↓
Evidence Collection
        ↓
Finding Classification
        ↓
Code / Prompt Generation
        ↓
Human Validation
        ↓
Report Export
```

---

## Data Handling

By default, the starter app stores records in Streamlit session state.

That means:

- records persist only for the active session
- exports should be downloaded before closing or refreshing the session
- no database is configured by default
- no external telemetry is implemented by default

For production use, add explicit persistence through a controlled backend such as SQLite, PostgreSQL, Supabase, or another approved datastore.

---

## Exported Artifacts

The current app can export:

- workflow prompts as Markdown
- findings as JSON
- findings as CSV
- findings as Markdown
- evidence ledger as JSON
- full report as Markdown

All exported artifacts should be reviewed before use in client reports, internal tickets, detection engineering tasks, or remediation workflows.

---

## Testing & Quality Checks

Suggested local checks:

```bash
python -m py_compile app.py
streamlit run app.py
```

Recommended future checks:

```bash
python -m pip install ruff pytest bandit pip-audit
ruff check .
bandit -r .
pip-audit
pytest
```

For now, the starter package is intentionally small, so the primary validation path is syntax checking plus manual UI testing.

---

## Development Roadmap

### Phase 1

- Scope-gated workflows
- Findings management
- Report export
- Prompt surface
- Evidence ledger

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
- confirm no unsafe workflow bypasses were introduced
- keep generated content reviewable by humans

---

## License

Licensed under the Apache 2.0 License.

See the LICENSE file for details.

---

## Disclaimer

This project is provided for authorized security research, defensive engineering, and educational purposes only.

The maintainers assume no liability for misuse, unauthorized deployment, or operational damage caused by derivative implementations.

Generated outputs may contain inaccuracies, insecure assumptions, or incomplete implementations.

Human review is required before production or operational use.

---

## Acknowledgements

Built with:

- Streamlit
- Hugging Face
- Python Software Foundation

Inspired by structured operational engineering, purple-team methodology, and the stubborn belief that security tooling should behave like systems engineering rather than ritual magic.