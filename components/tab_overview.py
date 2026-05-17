
import streamlit as st

from components.ui import render_metric_card
from utils.helpers import scope_is_unlocked
from utils.models import EvidenceEntry, Finding


def render_overview() -> None:
    """Render dashboard overview cards."""

    findings: list[Finding] = st.session_state.findings
    evidence: list[EvidenceEntry] = st.session_state.evidence

    col_a, col_b, col_c, col_d = st.columns(4)

    with col_a:
        status = "Unlocked" if scope_is_unlocked() else "Locked"
        render_metric_card("Scope status", status, "Authorization boundary")

    with col_b:
        render_metric_card("Findings", str(len(findings)), "Structured records")

    with col_c:
        render_metric_card("Evidence notes", str(len(evidence)), "Hash-linked ledger")

    with col_d:
        render_metric_card("Model profile", st.session_state.selected_model.split("/")[-1], "Prompt routing")

    st.divider()

    col_left, col_right = st.columns([1.2, 1])

    with col_left:
        st.subheader("Workflow Spine")
        st.markdown(
            """
            ```text
            Scope Definition
                    ↓
            Passive Recon Planning
                    ↓
            Evidence Collection
                    ↓
            Finding Classification
                    ↓
            Prompt / Code Drafting
                    ↓
            Human Validation
                    ↓
            Report Export
            ```
            """
        )

    with col_right:
        st.subheader("Operating Rules")
        st.markdown(
            """
            <div class="safe-box">
            <strong>Allowed:</strong> scoped planning, evidence handling,
            defensive validation, detection engineering, remediation, and report drafting.
            </div>
            <br />
            <div class="danger-box">
            <strong>Blocked:</strong> autonomous exploitation, credential theft,
            malware, persistence, destructive actions, and unscoped targets.
            </div>
            """,
            unsafe_allow_html=True,
        )
