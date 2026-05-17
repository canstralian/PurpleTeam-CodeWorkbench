import streamlit as st

from prompts.engine import generate_workflow_prompt
from utils.helpers import scope_is_unlocked


def render_workflow_builder() -> None:
    """Render safe workflow and prompt generation controls."""

    st.subheader("2. Workflow / Prompt Builder")

    if not scope_is_unlocked():
        st.warning("Create and confirm a scope gate before generating workflow artifacts.")
        return

    with st.form("workflow_builder"):
        col_a, col_b = st.columns([1, 1])

        with col_a:
            workflow_type = st.selectbox(
                "Workflow type",
                options=[
                    "Detection engineering plan",
                    "Passive recon planning brief",
                    "Finding triage brief",
                    "Remediation plan",
                    "Safe proof-of-concept pseudocode",
                    "Incident response tabletop",
                    "Report drafting prompt",
                ],
            )

            output_format = st.selectbox(
                "Output format",
                options=[
                    "Markdown report section",
                    "Step-by-step analyst checklist",
                    "JSON schema",
                    "Detection engineering ticket",
                    "Executive summary",
                ],
            )

        with col_b:
            objective = st.text_area(
                "Objective",
                placeholder=(
                    "Example: Draft a detection engineering plan for suspicious "
                    "login bursts in the staging environment."
                ),
                height=155,
            )

        trusted_context = st.text_area(
            "Trusted context",
            placeholder="Verified scope notes, logs summary, asset inventory, approved constraints.",
            height=120,
        )

        untrusted_context = st.text_area(
            "Untrusted context",
            placeholder="Raw tool output, copied web text, user-submitted reports, pasted terminal logs.",
            height=120,
        )

        submitted = st.form_submit_button("Generate workflow prompt")

    if submitted:
        if not objective.strip():
            st.error("Objective is required.")
            return

        prompt = generate_workflow_prompt(
            selected_model=st.session_state.selected_model,
            scope=st.session_state.scope,
            workflow_type=workflow_type,
            objective=objective,
            trusted_context=trusted_context,
            untrusted_context=untrusted_context,
            output_format=output_format,
        )

        st.session_state.last_prompt = prompt
        st.success("Workflow prompt generated.")

    if "last_prompt" in st.session_state:
        st.markdown("#### Generated Prompt")
        st.code(st.session_state.last_prompt, language="markdown")
        st.download_button(
            "Download prompt",
            data=st.session_state.last_prompt,
            file_name="purple_team_workflow_prompt.md",
            mime="text/markdown",
        )
