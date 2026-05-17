import pandas as pd
import streamlit as st

from utils.models import MODEL_ROLES


def render_model_profiles() -> None:
    """Render model profile and project settings information."""

    st.subheader("6. Model Profiles & Deployment Notes")

    st.write(
        "These profiles mirror the project README. The app does not call the models "
        "directly, because making external inference configuration implicit is how "
        "systems become haunted."
    )

    rows = [
        {"model": model, "purpose": purpose}
        for model, purpose in MODEL_ROLES.items()
    ]

    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

    st.markdown(
        """
        #### Suggested Hugging Face Space metadata

        ```yaml
        title: Purple Team Code Workbench
        emoji: 🛠️
        colorFrom: purple
        colorTo: indigo
        sdk: streamlit
        sdk_version: 1.57.0
        python_version: '3.11'
        app_file: app.py
        pinned: true
        license: apache-2.0
        short_description: AI workbench for purple-team security workflows.
        suggested_hardware: cpu-upgrade
        suggested_storage: small
        ```
        """
    )
