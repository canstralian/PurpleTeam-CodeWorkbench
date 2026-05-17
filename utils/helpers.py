
import streamlit as st

from utils.models import ScopeRecord


def scope_is_unlocked() -> bool:
    """Return whether a valid scope has been created."""

    scope: ScopeRecord | None = st.session_state.scope
    return bool(scope and scope.authorization_confirmed and scope.target_system)
