import json
from dataclasses import asdict
from datetime import datetime

import pandas as pd
import streamlit as st

from utils.export import records_to_csv, render_findings_markdown
from utils.helpers import scope_is_unlocked
from utils.models import Finding


def create_finding_id() -> str:
    """Create a stable-ish finding identifier for the current session."""

    next_number = len(st.session_state.findings) + 1
    return f"PTCW-{next_number:03d}"

def render_findings_manager() -> None:
    """Render finding creation, table display, and export controls."""

    st.subheader("3. Findings Manager")

    if not scope_is_unlocked():
        st.warning("Findings require a saved scope gate.")
        return

    with st.form("finding_form", clear_on_submit=True):
        col_a, col_b, col_c = st.columns(3)

        with col_a:
            title = st.text_input("Finding title")
            severity = st.selectbox(
                "Severity",
                options=["Informational", "Low", "Medium", "High", "Critical"],
                index=2,
            )

        with col_b:
            confidence = st.selectbox(
                "Confidence",
                options=["Low", "Medium", "High", "Confirmed"],
                index=1,
            )
            status = st.selectbox(
                "Status",
                options=["Draft", "Needs validation", "Validated", "Remediated", "Accepted risk"],
            )

        with col_c:
            affected_asset = st.text_input("Affected asset")

        summary = st.text_area("Summary", height=100)
        evidence = st.text_area("Evidence", height=120)
        impact = st.text_area("Impact", height=100)
        remediation = st.text_area("Remediation", height=100)
        validation_notes = st.text_area("Validation notes", height=100)

        submitted = st.form_submit_button("Add finding")

    if submitted:
        if not title.strip() or not summary.strip():
            st.error("Title and summary are required.")
            return

        finding = Finding(
            finding_id=create_finding_id(),
            title=title.strip(),
            severity=severity,
            confidence=confidence,
            status=status,
            affected_asset=affected_asset.strip(),
            summary=summary.strip(),
            evidence=evidence.strip(),
            impact=impact.strip(),
            remediation=remediation.strip(),
            validation_notes=validation_notes.strip(),
            created_at=datetime.utcnow().isoformat(timespec="seconds") + "Z",
        )
        st.session_state.findings.append(finding)
        st.success(f"Added finding {finding.finding_id}.")

    render_findings_table()


def render_findings_table() -> None:
    """Render findings table and export controls."""

    findings: list[Finding] = st.session_state.findings

    if not findings:
        st.info("No findings yet. The report goblin remains unfed.")
        return

    records = [asdict(finding) for finding in findings]
    frame = pd.DataFrame(records)

    st.dataframe(
        frame[
            [
                "finding_id",
                "title",
                "severity",
                "confidence",
                "status",
                "affected_asset",
                "created_at",
            ]
        ],
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("#### Expandable Details")
    for finding in findings:
        with st.expander(f"{finding.finding_id}: {finding.title} ({finding.severity})"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Confidence:** {finding.confidence}")
                st.write(f"**Status:** {finding.status}")
                st.write(f"**Affected Asset:** {finding.affected_asset or 'N/A'}")
            with col2:
                st.write(f"**Created:** {finding.created_at}")

            st.write("**Summary:**")
            st.write(finding.summary)
            st.write("**Impact:**")
            st.write(finding.impact or "N/A")
            st.write("**Remediation:**")
            st.write(finding.remediation or "N/A")

    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.download_button(
            "Export findings JSON",
            data=json.dumps(records, indent=2),
            file_name="findings.json",
            mime="application/json",
        )

    with col_b:
        st.download_button(
            "Export findings CSV",
            data=records_to_csv(records),
            file_name="findings.csv",
            mime="text/csv",
        )

    with col_c:
        st.download_button(
            "Export findings Markdown",
            data=render_findings_markdown(findings),
            file_name="findings.md",
            mime="text/markdown",
        )
