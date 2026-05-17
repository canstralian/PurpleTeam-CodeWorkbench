"""
components/sidebar.py
Sidebar navigation and global settings.
"""


import streamlit as st

from utils.models import DISALLOWED_ACTIONS, MODEL_ROLES, ScopeRecord


def render_sidebar() -> None:
    """Render navigation and global model settings."""

    with st.sidebar:
        st.header("Workbench Control")

        st.session_state.selected_model = st.selectbox(
            "Model profile",
            options=list(MODEL_ROLES.keys()),
            index=list(MODEL_ROLES.keys()).index(st.session_state.selected_model),
            help="This demo uses model profiles for prompt routing. It does not call external APIs.",
        )

        st.caption(MODEL_ROLES[st.session_state.selected_model])

        st.divider()

        scope: ScopeRecord | None = st.session_state.scope
        if scope and scope.authorization_confirmed:
            st.success("Scope gate unlocked")
            st.write(f"**Engagement:** {scope.engagement_name}")
            st.write(f"**Target:** {scope.target_system}")
        else:
            st.warning("Scope gate locked")

        st.divider()

        st.subheader("Hard non-goals")
        for item in DISALLOWED_ACTIONS:
            st.markdown(f"- {item}")

        st.divider()

        if st.button("Reset Session", type="primary", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
