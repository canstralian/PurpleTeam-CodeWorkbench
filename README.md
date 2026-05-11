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

# Purple Team Code Workbench - Streamlit Starter

This package contains a working Streamlit implementation based on the provided Purple Team Code Workbench project spec.

## Files

- `app.py` - main Streamlit application
- `requirements.txt` - Python dependencies
- `.streamlit/config.toml` - theme and server defaults

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

On Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Safety posture

The app intentionally avoids autonomous offensive execution. It is a scope-gated workflow, findings, evidence, and report workspace for authorized defensive/purple-team work.
