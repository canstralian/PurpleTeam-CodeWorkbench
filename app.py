"""
Purple Team Code Workbench
Streamlit application scaffold inspired by the generated dashboard mockup.

Run:
    streamlit run app.py
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

import pandas as pd
import streamlit as st


# -----------------------------------------------------------------------------
# Page configuration
# -----------------------------------------------------------------------------

st.set_page_config(
    page_title="Purple Team Code Workbench",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# -----------------------------------------------------------------------------
# Data models
# -----------------------------------------------------------------------------

@dataclass(frozen=True)
class WorkflowStep:
    number: int
    label: str
    status: str


@dataclass(frozen=True)
class EvidenceItem:
    evidence_id: str
    source: str
    evidence_type: str
    description: str
    risk_indicator: str
    collected_at: str


@dataclass(frozen=True)
class Finding:
    finding_id: str
    title: str
    description: str
    severity: str
    category: str
    status: str
    confidence: str
    updated_at: str


# -----------------------------------------------------------------------------
# Styling
# -----------------------------------------------------------------------------

CUSTOM_CSS = """
<style>
:root {
    --bg: #070914;
    --panel: #111827;
    --panel-soft: #151b2e;
    --border: #2a3147;
    --purple: #7c3aed;
    --purple-soft: #a855f7;
    --green: #22c55e;
    --yellow: #f59e0b;
    --red: #ef4444;
    --blue: #3b82f6;
    --text: #f8fafc;
    --muted: #94a3b8;
}

.stApp {
    background: radial-gradient(circle at top, #14112a 0%, #070914 42%, #050711 100%);
    color: var(--text);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #080b17 0%, #0d1020 100%);
    border-right: 1px solid var(--border);
}

.block-container {
    padding-top: 1.4rem;
    padding-bottom: 2rem;
}

.hero-title {
    font-size: 2rem;
    font-weight: 800;
    margin-bottom: 0.25rem;
}

.hero-subtitle {
    color: var(--muted);
    font-size: 0.95rem;
    margin-bottom: 1rem;
}

.panel {
    background: rgba(17, 24, 39, 0.88);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 1.1rem;
    box-shadow: 0 18px 50px rgba(0,0,0,0.35);
}

.metric-card {
    background: rgba(21, 27, 46, 0.9);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1rem;
    text-align: center;
}

.metric-card strong {
    font-size: 1.55rem;
    display: block;
}

.metric-card span {
    color: var(--muted);
    font-size: 0.82rem;
}

.workflow-row {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 0.5rem;
    margin: 1.2rem 0 1.6rem;
}

.workflow-step {
    flex: 1;
    text-align: center;
    position: relative;
}

.workflow-badge {
    width: 42px;
    height: 42px;
    margin: 0 auto 0.5rem;
    border-radius: 999px;
    border: 1px solid var(--border);
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: 800;
    background: #0b1020;
}

.workflow-step.complete .workflow-badge {
    border-color: var(--green);
    color: var(--green);
}

.workflow-step.active .workflow-badge {
    background: linear-gradient(135deg, var(--purple), var(--purple-soft));
    border-color: var(--purple-soft);
    color: white;
    box-shadow: 0 0 26px rgba(168, 85, 247, 0.65);
}

.workflow-step.pending .workflow-badge {
    color: var(--muted);
}

.workflow-label {
    font-size: 0.78rem;
    color: #dbeafe;
}

.status-pill {
    display: inline-flex;
    align-items: center;
    border-radius: 999px;
    padding: 0.16rem 0.5rem;
    font-size: 0.72rem;
    font-weight: 700;
}

.low { background: rgba(34,197,94,0.12); color: var(--green); border: 1px solid rgba(34,197,94,0.35); }
.medium { background: rgba(245,158,11,0.12); color: var(--yellow); border: 1px solid rgba(245,158,11,0.35); }
.high { background: rgba(239,68,68,0.12); color: var(--red); border: 1px solid rgba(239,68,68,0.35); }
.open { background: rgba(59,130,246,0.12); color: var(--blue); border: 1px solid rgba(59,130,246,0.35); }
.authorized { background: rgba(34,197,94,0.15); color: var(--green); border: 1px solid rgba(34,197,94,0.35); }

.scope-box {
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 0.85rem;
    background: rgba(17, 24, 39, 0.72);
    margin-top: 1rem;
}

.scope-label {
    color: var(--muted);
    font-size: 0.74rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.scope-value {
    font-weight: 700;
    margin-bottom: 0.45rem;
}

hr {
    border-color: var(--border);
}

.stButton > button {
    border-radius: 12px;
    border: 1px solid var(--border);
    background: linear-gradient(135deg, #6d28d9, #9333ea);
    color: white;
    font-weight: 700;
}

.stButton > button:hover {
    border-color: #c084fc;
    color: white;
}

[data-testid="stDataFrame"] {
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# Seed data
# -----------------------------------------------------------------------------

WORKFLOW_STEPS: List[WorkflowStep] = [
    WorkflowStep(1, "Scope Definition", "complete"),
    WorkflowStep(2, "Passive Recon", "complete"),
    WorkflowStep(3, "Evidence Collection", "complete"),
    WorkflowStep(4, "Finding Classification", "active"),
    WorkflowStep(5, "Code / Prompt Generation", "pending"),
    WorkflowStep(6, "Human Validation", "pending"),
    WorkflowStep(7, "Report Export", "pending"),
]

EVIDENCE_ITEMS: List[EvidenceItem] = [
    EvidenceItem("EV-1001", "nmap", "Open Port", "Port 22 SSH is open on 10.10.0.15", "Low", "2024-05-17 09:12"),
    EvidenceItem("EV-1002", "nuclei", "CVE", "CVE-2023-28432 detected on web server", "Medium", "2024-05-17 09:18"),
    EvidenceItem("EV-1003", "whatweb", "Tech Fingerprint", "Apache/2.4.49 identified", "Low", "2024-05-17 09:20"),
    EvidenceItem("EV-1004", "gobuster", "Directory", "/admin panel discovered with HTTP 200", "Medium", "2024-05-17 09:22"),
    EvidenceItem("EV-1005", "nmap", "Service Version", "OpenSSH 7.6p1 Ubuntu 4ubuntu0.3", "Low", "2024-05-17 09:23"),
]

FINDINGS: List[Finding] = [
    Finding("F-1001", "Exposed SSH Service", "SSH service exposed to internal network", "Low", "Configuration", "Open", "High", "2024-05-17 09:25"),
    Finding("F-1002", "Outdated Apache Version", "Apache 2.4.49 with known vulnerabilities", "Medium", "Vulnerability", "Open", "Medium", "2024-05-17 09:26"),
    Finding("F-1003", "Directory Listing Enabled", "/admin directory is publicly accessible", "Medium", "Configuration", "Open", "Medium", "2024-05-17 09:27"),
    Finding("F-1004", "Information Disclosure", "Server version disclosure in headers", "Low", "Information Disclosure", "Open", "High", "2024-05-17 09:28"),
    Finding("F-1005", "Potential Default Credentials", "Default admin panel detected", "High", "Authentication", "Open", "Medium", "2024-05-17 09:29"),
]

MODEL_OPTIONS = [
    "DeepHat-V1-7B",
    "Gemma-4-E4B-Uncensored",
    "Meta-Llama-3-8B-Instruct",
]


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def to_dataframe(items: List[object]) -> pd.DataFrame:
    """Convert dataclass objects into a DataFrame."""
    return pd.DataFrame([item.__dict__ for item in items])


def severity_class(value: str) -> str:
    """Return a CSS class for a severity value."""
    return value.lower().strip()


def pill(label: str, css_class: str | None = None) -> str:
    """Render a small HTML pill."""
    css_class = css_class or label.lower().strip()
    return f'<span class="status-pill {css_class}">{label}</span>'


def render_workflow_steps(steps: List[WorkflowStep]) -> None:
    """Render the workflow progress tracker."""
    html = '<div class="workflow-row">'
    for step in steps:
        html += f"""
        <div class="workflow-step {step.status}">
            <div class="workflow-badge">{step.number}</div>
            <div class="workflow-label">{step.label}</div>
        </div>
        """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def render_scope_box() -> None:
    """Render active scope information in the sidebar."""
    st.markdown(
        """
        <div class="scope-box">
            <div style="display:flex;justify-content:space-between;align-items:center;">
                <div class="scope-label">Active Scope</div>
                <span class="status-pill authorized">Authorized</span>
            </div>
            <hr />
            <div class="scope-label">Engagement</div>
            <div class="scope-value">Internal Infra Assessment</div>
            <div class="scope-label">Scope ID</div>
            <div class="scope-value">PT-2024-05-17</div>
            <div class="scope-label">Target</div>
            <div class="scope-value">10.10.0.0/16</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_report_preview(findings: List[Finding]) -> None:
    """Render a compact report preview panel."""
    high = sum(1 for finding in findings if finding.severity == "High")
    medium = sum(1 for finding in findings if finding.severity == "Medium")
    low = sum(1 for finding in findings if finding.severity == "Low")

    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.subheader("Internal Infra Assessment Report")
    st.caption("Scope ID: PT-2024-05-17")
    st.caption(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><strong>15</strong><span>Total Findings</span></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><strong>{high}</strong><span>High</span></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card"><strong>{medium}</strong><span>Medium</span></div>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<div class="metric-card"><strong>{low}</strong><span>Low</span></div>', unsafe_allow_html=True)

    st.markdown("### Top Findings")
    for finding in findings:
        if finding.severity in {"High", "Medium"}:
            st.markdown(
                f"- `{finding.finding_id}` **{finding.title}** "
                f"{pill(finding.severity, severity_class(finding.severity))}",
                unsafe_allow_html=True,
            )

    st.download_button(
        "Export Report (Markdown)",
        data=generate_markdown_report(findings),
        file_name="purple-team-report.md",
        mime="text/markdown",
        use_container_width=True,
    )

    if st.button("Copy Report to Clipboard", use_container_width=True):
        st.toast("Report text prepared. Browser clipboard integration requires a custom component.")

    st.markdown('</div>', unsafe_allow_html=True)


def generate_markdown_report(findings: List[Finding]) -> str:
    """Generate a markdown report from the current findings."""
    lines = [
        "# Internal Infra Assessment Report",
        "",
        "**Scope ID:** PT-2024-05-17",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Summary",
        "",
        f"Total findings: {len(findings)}",
        "",
        "## Findings",
        "",
    ]

    for finding in findings:
        lines.extend(
            [
                f"### {finding.finding_id}: {finding.title}",
                "",
                f"- Severity: {finding.severity}",
                f"- Category: {finding.category}",
                f"- Status: {finding.status}",
                f"- Confidence: {finding.confidence}",
                f"- Updated: {finding.updated_at}",
                "",
                finding.description,
                "",
            ]
        )

    return "\n".join(lines)


# -----------------------------------------------------------------------------
# Sidebar
# -----------------------------------------------------------------------------

with st.sidebar:
    st.markdown("## Purple Team\n## Code Workbench")
    st.caption("Authorized security workflow surface")
    st.divider()

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Scope & Targets",
            "Workflows",
            "Code Generation",
            "Tools",
            "Findings",
            "Reports",
            "Settings",
        ],
        index=2,
    )

    render_scope_box()

    st.divider()
    st.caption("Operator")
    st.write("analyst@corp.local")


# -----------------------------------------------------------------------------
# Main pages
# -----------------------------------------------------------------------------

selected_model = st.selectbox("Model", MODEL_OPTIONS, index=0)

if page == "Dashboard":
    st.markdown('<div class="hero-title">Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Current engagement status, scope posture, and findings summary.</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><strong>7</strong><span>Workflow Steps</span></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><strong>5</strong><span>Evidence Items</span></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><strong>5</strong><span>Open Findings</span></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><strong>1</strong><span>High Severity</span></div>', unsafe_allow_html=True)

    st.write("")
    render_workflow_steps(WORKFLOW_STEPS)

elif page == "Workflows":
    st.markdown('<div class="hero-title">Workflow Orchestrator</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-subtitle">Execute and track purple-team workflows with human-in-the-loop control.</div>',
        unsafe_allow_html=True,
    )

    render_workflow_steps(WORKFLOW_STEPS)

    left, right = st.columns([2.4, 1])

    with left:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.subheader("Step 4: Finding Classification")
        st.caption("Review collected evidence and classify potential findings.")

        tabs = st.tabs(["Collected Evidence", "Classification", "Notes"])
        with tabs[0]:
            st.dataframe(
                to_dataframe(EVIDENCE_ITEMS).rename(
                    columns={
                        "evidence_id": "ID",
                        "source": "Source",
                        "evidence_type": "Type",
                        "description": "Description",
                        "risk_indicator": "Risk Indicator",
                        "collected_at": "Collected At",
                    }
                ),
                use_container_width=True,
                hide_index=True,
            )
            st.caption("Showing 1 to 5 of 12 evidence items")

        with tabs[1]:
            selected_evidence = st.selectbox(
                "Evidence item",
                [item.evidence_id for item in EVIDENCE_ITEMS],
            )
            severity = st.selectbox("Proposed severity", ["Low", "Medium", "High"])
            category = st.selectbox(
                "Category",
                ["Configuration", "Vulnerability", "Authentication", "Information Disclosure"],
            )
            if st.button("Create Draft Finding"):
                st.toast(f"Draft finding created from {selected_evidence} as {severity}/{category}.")

        with tabs[2]:
            st.text_area(
                "Analyst notes",
                value="Review evidence relationships before escalating to code/prompt generation.",
                height=140,
            )

        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.subheader("Workflow Control")
        st.caption("Internal Infra Assessment")
        st.write(f"**Status:** {pill('In Progress', 'open')}", unsafe_allow_html=True)
        st.write("**Current Step:** 4 of 7 - Finding Classification")
        st.write("**Started At:** 2024-05-17 09:02")
        st.write("**Last Updated:** 2024-05-17 09:24")
        st.button("Continue to Next Step →", use_container_width=True)
        st.button("← Back to Previous Step", use_container_width=True)
        st.button("Pause Workflow", use_container_width=True)
        st.info("Review each evidence item and classify it according to severity and impact.")
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "Findings":
    st.markdown('<div class="hero-title">Findings</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Manage, review, and export engagement findings.</div>', unsafe_allow_html=True)

    left, right = st.columns([2.1, 1])

    with left:
        tab_all, tab_severity, tab_status, tab_category = st.tabs(
            ["All Findings", "By Severity", "By Status", "By Category"]
        )
        with tab_all:
            search = st.text_input("Search findings", placeholder="Search findings...")
            findings_df = to_dataframe(FINDINGS).rename(
                columns={
                    "finding_id": "ID",
                    "title": "Title",
                    "description": "Description",
                    "severity": "Severity",
                    "category": "Category",
                    "status": "Status",
                    "confidence": "Confidence",
                    "updated_at": "Updated At",
                }
            )
            if search:
                findings_df = findings_df[
                    findings_df.apply(
                        lambda row: search.lower() in " ".join(str(v).lower() for v in row.values),
                        axis=1,
                    )
                ]
            st.dataframe(findings_df, use_container_width=True, hide_index=True)
            st.caption("Showing 1 to 5 of 15 findings")

        with tab_severity:
            st.bar_chart(to_dataframe(FINDINGS)["severity"].value_counts())

        with tab_status:
            st.bar_chart(to_dataframe(FINDINGS)["status"].value_counts())

        with tab_category:
            st.bar_chart(to_dataframe(FINDINGS)["category"].value_counts())

    with right:
        render_report_preview(FINDINGS)

elif page == "Reports":
    st.markdown('<div class="hero-title">Reports</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Preview and export structured engagement reports.</div>', unsafe_allow_html=True)
    render_report_preview(FINDINGS)

elif page == "Code Generation":
    st.markdown('<div class="hero-title">Code Generation</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Draft controlled code and prompt artifacts for authorized workflows.</div>', unsafe_allow_html=True)

    with st.form("code_generation_form"):
        objective = st.text_area(
            "Authorized objective",
            placeholder="Describe the defensive workflow, validation task, or report artifact you want to generate.",
            height=120,
        )
        guardrails = st.multiselect(
            "Guardrails",
            [
                "No autonomous execution",
                "No credential handling",
                "Passive-only mode",
                "Human validation required",
                "Generate report artifact only",
            ],
            default=["Human validation required", "No autonomous execution"],
        )
        submitted = st.form_submit_button("Generate Draft")

    if submitted:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.subheader("Generated Draft")
        st.code(
            """# Draft placeholder\n# Replace this section with provider-backed generation.\n# Objective and guardrails should be sent as structured context.\n""",
            language="python",
        )
        st.write("**Objective:**", objective or "No objective provided")
        st.write("**Guardrails:**", ", ".join(guardrails))
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown(f'<div class="hero-title">{page}</div>', unsafe_allow_html=True)
    st.info("This section is scaffolded for future implementation.")


# -----------------------------------------------------------------------------
# Footer
# -----------------------------------------------------------------------------

st.caption(
    "Purple Team Code Workbench · Authorized workflows only · Generated outputs require human review."
)
