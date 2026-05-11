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
