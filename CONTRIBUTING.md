# Contributing to Purple Team Code Workbench

Thank you for your interest in contributing to the Purple Team Code Workbench! We welcome contributions that improve the project's safety, clarity, and effectiveness for authorized security research.

## Code of Conduct

Please be respectful and professional in all interactions.

## How to Contribute

1.  **Report Bugs:** Use the GitHub Issues to report bugs. Provide as much detail as possible, including steps to reproduce.
2.  **Suggest Features:** We welcome feature suggestions! Please open an issue to discuss your idea before starting work.
3.  **Submit Pull Requests:**
    *   Fork the repository and create a new branch for your change.
    *   Ensure your code follows the project's style (run `ruff check .`).
    *   Ensure all tests pass (run `pytest`).
    *   Add tests for any new functionality.
    *   Include type hints (run `mypy .`).
    *   Write clear, concise commit messages.

## Development Setup

1.  Clone the repository.
2.  Create a virtual environment: `python -m venv .venv`.
3.  Activate the environment.
4.  Install dependencies: `pip install -r requirements.txt`.
5.  Install development tools: `pip install ruff mypy pytest pip-audit`.

## Safety Guidelines

This project is for **authorized security work only**.
- Never contribute code that enables unauthorized access, malware deployment, or other malicious activities.
- Prioritize human-in-the-loop controls and operational traceability.
- Ensure that generated artifacts are always clearly marked as needing human validation.

## License

By contributing, you agree that your contributions will be licensed under the project's Apache 2.0 License.
