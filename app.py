"""
app.py
Purple Team Code Workbench.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from __future__ import annotations

from typing import Any

import streamlit as st

from components.header import render_hero
from components.sidebar import render_sidebar
from components.tab_evidence import render_evidence_ledger
from components.tab_findings import render_findings_manager
from components.tab_models import render_model_profiles
from components.tab_overview import render_overview
from components.tab_report import render_report_export
from components.tab_scope import render_scope_gate
from components.tab_workflow import render_workflow_builder
from components.ui import inject_styles
from utils.models import APP_SUBTITLE, APP_TITLE


def init_state() -> None:
    """Initialise Streamlit session state keys."""

    defaults: dict[str, Any] = {
        "scope": None,
        "findings": [],
        "evidence": [],
        "selected_model": "DeepHat/DeepHat-V1-7B",
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def apply_page_config() -> None:
    """Set page metadata and layout."""

    st.set_page_config(
        page_title=APP_TITLE,
        page_icon="🛠️",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def main() -> None:
    """Run the Streamlit app."""

    apply_page_config()
    init_state()
    inject_styles()
    render_hero(APP_TITLE, APP_SUBTITLE)
    render_sidebar()

    tabs = st.tabs(
        [
            "Overview",
            "Scope Gate",
            "Workflow Builder",
            "Findings",
            "Evidence Ledger",
            "Report Export",
            "Models",
        ]
    )

    with tabs[0]:
        render_overview()

    with tabs[1]:
        render_scope_gate()

    with tabs[2]:
        render_workflow_builder()

    with tabs[3]:
        render_findings_manager()

    with tabs[4]:
        render_evidence_ledger()

    with tabs[5]:
        render_report_export()

    with tabs[6]:
        render_model_profiles()


if __name__ == "__main__":
    main()
