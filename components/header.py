"""
components/header.py
UI header components.
"""

import streamlit as st


def render_hero(title: str, subtitle: str) -> None:
    """Render the application hero header."""

    st.markdown(
        f"""
        <div class="hero">
            <h1>{title}</h1>
            <p>{subtitle}</p>
            <p class="small-muted">
                Generation is not execution. Scope first, validate always,
                export only after human review.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
