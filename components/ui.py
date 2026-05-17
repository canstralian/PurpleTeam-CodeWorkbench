import streamlit as st


def inject_styles() -> None:
    """Inject lightweight CSS for dashboard-like visual structure."""

    st.markdown(
        """
        <style>
        :root {
            --card-bg: #111827;
            --card-border: #312e81;
            --muted-text: #c7d2fe;
            --accent: #8b5cf6;
            --success: #22c55e;
            --warning: #f59e0b;
            --danger: #ef4444;
        }

        .hero {
            padding: 1.4rem 1.6rem;
            border-radius: 1.1rem;
            background:
                radial-gradient(circle at top left, rgba(139, 92, 246, .34), transparent 35%),
                linear-gradient(135deg, #111827 0%, #1e1b4b 52%, #111827 100%);
            border: 1px solid rgba(167, 139, 250, .35);
            margin-bottom: 1rem;
        }

        .hero h1 {
            margin-bottom: .25rem;
        }

        .hero p {
            color: #ddd6fe;
            font-size: 1rem;
        }

        .metric-card {
            padding: 1rem;
            border-radius: 1rem;
            background: #111827;
            border: 1px solid rgba(167, 139, 250, .25);
            min-height: 120px;
        }

        .metric-card .label {
            color: #c4b5fd;
            font-size: .82rem;
            text-transform: uppercase;
            letter-spacing: .08em;
            margin-bottom: .4rem;
        }

        .metric-card .value {
            color: #ffffff;
            font-size: 1.6rem;
            font-weight: 700;
        }

        .small-muted {
            color: #a5b4fc;
            font-size: .86rem;
        }

        .safe-box {
            border-left: 4px solid #22c55e;
            padding: .75rem 1rem;
            background: rgba(34, 197, 94, .08);
            border-radius: .6rem;
        }

        .danger-box {
            border-left: 4px solid #ef4444;
            padding: .75rem 1rem;
            background: rgba(239, 68, 68, .08);
            border-radius: .6rem;
        }

        .code-frame {
            border-radius: .8rem;
            border: 1px solid rgba(167, 139, 250, .25);
            padding: .7rem;
            background: #020617;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def render_metric_card(label: str, value: str, caption: str) -> None:
    """Render a dashboard metric card."""

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="label">{label}</div>
            <div class="value">{value}</div>
            <div class="small-muted">{caption}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
