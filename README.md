---
title: Uncensored HackerCoding GPT
emoji: 📉
colorFrom: pink
colorTo: pink
sdk: streamlit
sdk_version: 1.57.0
app_file: app.py
pinned: false
license: apache-2.0
short_description: Streamlitj  code-gen surface for purple team work.
---
---
title: Uncensored HackerCoding GPT
emoji: 📉
colorFrom: pink
colorTo: pink
sdk: streamlit
sdk_version: 1.57.0
app_file: app.py
pinned: false
license: apache-2.0
short_description: Streamlitj  code-gen surface for purple team work.

# Uncensored HackerCoding GPT

> A Streamlit code-generation surface for security research and purple team workflows. Built for operators who need a model that engages with offensive and defensive code without refusing the task.

**Live Space:** https://s-dreamer-uncensored-hackercoding.hf.space

-----

## Status

UI scaffold. `generate_code()` and `refine_code()` return placeholder strings — no model is wired in yet. The interface, sidebar, refine loop, session state, and download path are functional. See [Wire in a model](#wire-in-a-model).

-----

## Why this exists

General-purpose code assistants refuse a large class of legitimate security tasks:

- Writing a Suricata or YARA rule that requires understanding a malware sample
- Drafting a PoC for an authorized engagement
- Explaining an exploit chain end-to-end so you can write the detection for it
- Generating a fuzzer harness for a known-vulnerable function
- Producing payloads inside a CTF or lab boundary

This Space pairs a low-friction prompt UI with a model that doesn’t reflexively refuse those workflows. The tradeoff: every output is your responsibility. There is no model-side guardrail catching mistakes, scope violations, or bad ideas. Read what you ship.

-----

## In scope

- Detection engineering: YARA, Sigma, Suricata, Snort, Splunk SPL, KQL, osquery
- Offensive PoCs against systems you own or are explicitly authorized to test
- CVE analysis and reproduction in a lab
- Fuzzer harnesses (libFuzzer, AFL++, Honggfuzz, boofuzz)
- Hardening patches, sandbox escapes-then-fixes, secure coding refactors
- IR and forensics tooling: log parsers, timeline builders, memory triage scripts
- CTF challenge work
- Red team tooling for authorized engagements
- Adversarial ML probes against your own models

## Out of scope

- Targeting systems you do not own and are not authorized to test
- Generating malware for deployment against third parties
- Bypassing controls in production systems you don’t operate
- Anything that would put a real user, customer, or bystander at risk

These are not features the tool blocks. They are commitments the operator makes.

-----

## Run locally

```bash
git clone https://huggingface.co/spaces/S-Dreamer/Uncensored-HackerCoding
cd Uncensored-HackerCoding
pip install streamlit==1.57.0
streamlit run app.py
```

Opens at `http://localhost:8501`.

-----

## UI reference

### Sidebar settings

|Control      |Values                                                                          |Default           |
|-------------|--------------------------------------------------------------------------------|------------------|
|Language     |`Python`, `JavaScript`, `TypeScript`, `SQL`, `Bash`, `HTML/CSS`                 |`Python`          |
|Output style |`Clean and simple`, `Beginner-friendly`, `Production-ready`, `Heavily commented`|`Clean and simple`|
|Include tests|bool                                                                            |`false`           |

### Output tabs

|Tab    |Purpose                                                                          |
|-------|---------------------------------------------------------------------------------|
|Code   |Renders output via `st.code()`, syntax-highlighted by selected language          |
|Refine |Submits a refinement prompt; result replaces the previous output in session state|
|Actions|Download as `generated_code.txt` or clear the output                             |

### Recommended additions for security workflows

Replace the `language` and `examples` lists in `app.py` with sec-research-relevant options:

```python
language = st.selectbox(
    "Language",
    ["Python", "C", "C++", "Go", "Rust", "Bash", "PowerShell",
     "Assembly (x86_64)", "YARA", "Sigma", "Suricata", "KQL", "Splunk SPL"]
)

examples = [
    "Write a YARA rule that detects PE files with a high-entropy .text section and an imported VirtualAllocEx.",
    "Generate a libFuzzer harness for a function with signature `int parse_packet(const uint8_t *buf, size_t len)`.",
    "Write a Sigma rule for suspicious child processes spawned by Outlook on Windows.",
    "Draft a Python script that parses Sysmon EVTX logs and flags Event ID 1 with unusual parent-child pairs.",
]
```

-----

## Wire in a model

Both functions take strings and return a string. Replace their bodies with a model call.

`generate_code(prompt, language, style, include_tests)` — `app.py:3`
`refine_code(existing_code, refinement_prompt, language)` — `app.py:12`

Recommended backends (security-research-tuned or instruct-grade with low refusal rate on sec topics):

|Model                                            |Notes                                                    |
|-------------------------------------------------|---------------------------------------------------------|
|`WhiteRabbitNeo/WhiteRabbitNeo-13B-v1`           |Sec-focused fine-tune, strong on offensive/defensive code|
|`cognitivecomputations/dolphin-2.9.4-llama3.1-8b`|General uncensored instruct, decent code performance     |
|`bigcode/starcoder2-15b-instruct-v0.1`           |Stronger raw code, less topical refusal than chat models |

Example with the HF Inference API:

```python
import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    model="WhiteRabbitNeo/WhiteRabbitNeo-13B-v1",
    token=os.environ["HF_TOKEN"],
)

def generate_code(prompt: str, language: str, style: str, include_tests: bool) -> str:
    system = (
        f"You are a security research code generator. "
        f"Target language: {language}. Style: {style}. "
        f"{'Include tests.' if include_tests else 'Tests not required.'} "
        f"Return code only, no commentary."
    )
    response = client.chat_completion(
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        max_tokens=2048,
        temperature=0.2,
    )
    return response.choices[0].message.content
```

Add to `requirements.txt`:

```
streamlit==1.57.0
huggingface_hub>=0.24.0
```

Set `HF_TOKEN` as a Space secret under **Settings → Variables and secrets**.

-----

## Operating model

Treat every generated artifact as untrusted input until reviewed:

1. Read it before you run it. The model will produce confident-looking code that does the wrong thing.
1. Run it in an isolated environment first — VM, container, lab network. Never paste output directly into production.
1. Keep an authorization paper trail for anything you generate that touches a real target. Engagement letter, scope document, screenshot of the bug bounty program scope at the time of testing.
1. Static-analyze before committing. `bandit` for Python, `semgrep` for cross-language, `ruff` for hygiene.

-----

## License

Apache-2.0 — see <LICENSE>.

-----

## Disclaimer

Provided as-is, without warranty. The author is not liable for misuse, damages, or losses arising from use of this Space or any code it produces. The operator is solely responsible for ensuring all use is legal, authorized, and within scope of a documented engagement, lab boundary, or system they own.