"""
components/tab_evidence.py
Evidence ledger UI component.
"""

import json
from dataclasses import asdict
from datetime import datetime

import pandas as pd
import streamlit as st

from utils.crypto import compute_entry_hash
from utils.helpers import scope_is_unlocked
from utils.models import EvidenceEntry


def render_evidence_ledger() -> None:
    """Render hash-linked evidence ledger controls."""

    st.subheader("4. Evidence Ledger")

    if not scope_is_unlocked():
        st.warning("Evidence notes require a saved scope gate.")
        return

    with st.form("evidence_form", clear_on_submit=True):
        col_a, col_b = st.columns([1, 1])
        with col_a:
            category = st.selectbox(
                "Category",
                options=["Observation", "Log note", "Screenshot note", "Finding evidence", "Remediation evidence"],
            )
        with col_b:
            source = st.text_input(
                "Source",
                placeholder="Example: SIEM query, analyst note, screenshot filename",
            )

        description = st.text_area(
            "Description",
            placeholder="Record what was observed, by whom, and why it matters.",
            height=130,
        )

        submitted = st.form_submit_button("Append evidence entry")

    if submitted:
        if not description.strip():
            st.error("Evidence description is required.")
            return

        previous_hash = (
            st.session_state.evidence[-1].entry_hash
            if st.session_state.evidence
            else "GENESIS"
        )
        created_at = datetime.utcnow().isoformat(timespec="seconds") + "Z"
        entry_id = f"EVD-{len(st.session_state.evidence) + 1:03d}"
        entry_hash = compute_entry_hash(
            entry_id=entry_id,
            category=category,
            description=description.strip(),
            source=source.strip(),
            previous_hash=previous_hash,
            created_at=created_at,
        )

        entry = EvidenceEntry(
            entry_id=entry_id,
            category=category,
            description=description.strip(),
            source=source.strip(),
            previous_hash=previous_hash,
            entry_hash=entry_hash,
            created_at=created_at,
        )
        st.session_state.evidence.append(entry)
        st.success(f"Evidence entry {entry_id} appended.")

    evidence: list[EvidenceEntry] = st.session_state.evidence
    if not evidence:
        st.info("No evidence entries yet.")
        return

    records = [asdict(entry) for entry in evidence]
    st.dataframe(pd.DataFrame(records), use_container_width=True, hide_index=True)

    st.markdown("#### Expandable Ledger Details")
    for entry in evidence:
        with st.expander(f"{entry.entry_id}: {entry.category}"):
            st.write(f"**Source:** {entry.source or 'N/A'}")
            st.write(f"**Created:** {entry.created_at}")
            st.write(f"**Previous Hash:** `{entry.previous_hash}`")
            st.write(f"**Entry Hash:** `{entry.entry_hash}`")
            st.write("**Description:**")
            st.write(entry.description)

    st.download_button(
        "Export evidence ledger JSON",
        data=json.dumps(records, indent=2),
        file_name="evidence_ledger.json",
        mime="application/json",
    )
