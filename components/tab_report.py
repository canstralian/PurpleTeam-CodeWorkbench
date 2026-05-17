import streamlit as st

from utils.helpers import scope_is_unlocked
from utils.reporting import build_report_markdown


def render_report_export() -> None:
    """Render report preview and Markdown export."""

    st.subheader("5. Report Export")

    if not scope_is_unlocked():
        st.warning("Reports require a saved scope gate.")
        return

    report = build_report_markdown(
        scope=st.session_state.scope,
        findings=st.session_state.findings,
        evidence=st.session_state.evidence
    )

    st.markdown("#### Report Preview")
    st.markdown(report)

    st.download_button(
        "Download report Markdown",
        data=report,
        file_name="purple_team_report.md",
        mime="text/markdown",
    )
