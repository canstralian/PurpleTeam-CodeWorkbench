from dataclasses import asdict
from datetime import date, datetime

import streamlit as st

from utils.models import ALLOWED_ACTIONS, ScopeRecord


def create_scope_record(
    engagement_name: str,
    target_system: str,
    authorization_owner: str,
    start_date_value: date,
    end_date_value: date,
    allowed_actions: list[str],
    constraints: str,
    authorization_confirmed: bool,
) -> ScopeRecord:
    """Create a scope record from form input."""

    return ScopeRecord(
        engagement_name=engagement_name.strip(),
        target_system=target_system.strip(),
        authorization_owner=authorization_owner.strip(),
        start_date=start_date_value.isoformat(),
        end_date=end_date_value.isoformat(),
        allowed_actions=allowed_actions,
        constraints=constraints.strip(),
        authorization_confirmed=authorization_confirmed,
        created_at=datetime.utcnow().isoformat(timespec="seconds") + "Z",
    )

def render_scope_gate() -> None:
    """Render the scope-gating interface."""

    st.subheader("1. Scope Gate")
    st.write(
        "Define the authorization boundary before generating workflow material. "
        "Primitive, yes, but civilisation depends on forms now."
    )

    with st.form("scope_form", clear_on_submit=False):
        col_a, col_b = st.columns(2)

        with col_a:
            engagement_name = st.text_input(
                "Engagement name",
                value="Purple Team Validation Sprint",
            )
            target_system = st.text_input(
                "Authorized target / system",
                placeholder="Example: staging.example.com, internal lab range, customer-approved asset",
            )
            authorization_owner = st.text_input(
                "Authorization owner",
                placeholder="Name or team responsible for approval",
            )

        with col_b:
            start_date_value = st.date_input("Start date", value=date.today())
            end_date_value = st.date_input("End date", value=date.today())
            allowed_actions = st.multiselect(
                "Allowed action set",
                options=ALLOWED_ACTIONS,
                default=[
                    "Passive reconnaissance planning",
                    "Detection engineering",
                    "Finding classification",
                    "Report drafting",
                ],
            )

        constraints = st.text_area(
            "Constraints / exclusions",
            placeholder=(
                "Example: no production traffic, no credential attacks, "
                "no destructive testing, only approved assets."
            ),
            height=120,
        )

        authorization_confirmed = st.checkbox(
            "I confirm this work is authorized and limited to the defined scope."
        )

        submitted = st.form_submit_button("Save scope gate")

    if submitted:
        if not engagement_name.strip() or not target_system.strip():
            st.error("Engagement name and target/system are required.")
            return

        if end_date_value < start_date_value:
            st.error("End date cannot be before start date.")
            return

        if not allowed_actions:
            st.error("Select at least one allowed action. An empty permission set is just theatre.")
            return

        if not authorization_confirmed:
            st.error("Authorization confirmation is required before unlocking workflows.")
            return

        st.session_state.scope = create_scope_record(
            engagement_name=engagement_name,
            target_system=target_system,
            authorization_owner=authorization_owner,
            start_date_value=start_date_value,
            end_date_value=end_date_value,
            allowed_actions=allowed_actions,
            constraints=constraints,
            authorization_confirmed=authorization_confirmed,
        )
        st.success("Scope saved. Workflow generation is now unlocked.")

    if st.session_state.scope:
        st.markdown("#### Current Scope")
        st.json(asdict(st.session_state.scope), expanded=False)
