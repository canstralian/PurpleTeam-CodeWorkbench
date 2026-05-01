import streamlit as st

def generate_code(prompt: str, language: str, style: str, include_tests: bool) -> str:
    tests_note = "Include tests" if include_tests else "No tests requested"

    return f"""# Language: {language}
# Style: {style}
# {tests_note}

# Generated Code for:
# {prompt}
"""

def refine_code(existing_code: str, refinement_prompt: str, language: str) -> str:
    return f"""# Refined {language} Code
# Refinement request:
# {refinement_prompt}

{existing_code}

# Applied refinement:
# {refinement_prompt}
"""

st.set_page_config(
    page_title="Code Assistant",
    page_icon="💻",
    layout="wide"
)

if "prompt" not in st.session_state:
    st.session_state["prompt"] = ""

if "generated_code" not in st.session_state:
    st.session_state["generated_code"] = ""

st.title("Code Assistant")
st.caption("Generate, refine, and export code from natural-language prompts.")

with st.sidebar:
    st.header("Settings")

    language = st.selectbox(
        "Language",
        ["Python", "JavaScript", "TypeScript", "SQL", "Bash", "HTML/CSS"]
    )

    style = st.selectbox(
        "Output style",
        ["Clean and simple", "Beginner-friendly", "Production-ready", "Heavily commented"]
    )

    include_tests = st.checkbox("Include tests", value=False)

    st.divider()
    st.header("Prompt examples")

    examples = [
        "Write a Python function that validates email addresses and includes tests.",
        "Create a Streamlit app that uploads a CSV and plots summary statistics.",
        "Refactor this JavaScript function to be easier to read.",
        "Write a SQL query to find monthly recurring revenue by customer."
    ]

    for i, example in enumerate(examples):
        if st.button(example, key=f"example_{i}"):
            st.session_state["prompt"] = example

prompt = st.text_area(
    "Coding prompt",
    key="prompt",
    placeholder="Describe the code you want generated...",
    height=170
)

generate_clicked = st.button("Generate", type="primary")

if generate_clicked:
    if not prompt.strip():
        st.warning("Please enter a coding prompt first.")
    else:
        with st.spinner("Generating code..."):
            st.session_state["generated_code"] = generate_code(
                prompt,
                language,
                style,
                include_tests
            )

if st.session_state["generated_code"]:
    st.subheader("Generated output")

    tab_code, tab_refine, tab_actions = st.tabs(["Code", "Refine", "Actions"])

    with tab_code:
        st.code(st.session_state["generated_code"], language=language.lower())

    with tab_refine:
        refinement_prompt = st.text_area(
            "Refinement request",
            placeholder="Example: Add error handling, make it async, improve readability, or add type hints.",
            height=120
        )

        if st.button("Apply refinement", type="primary"):
            if not refinement_prompt.strip():
                st.warning("Please enter a refinement request first.")
            else:
                with st.spinner("Refining code..."):
                    st.session_state["generated_code"] = refine_code(
                        st.session_state["generated_code"],
                        refinement_prompt,
                        language
                    )

                st.success("Refinement applied.")
                st.rerun()

    with tab_actions:
        st.download_button(
            label="Download code",
            data=st.session_state["generated_code"],
            file_name="generated_code.txt",
            mime="text/plain"
        )

        if st.button("Clear output"):
            st.session_state["generated_code"] = ""
            st.rerun()
else:
    st.info("Choose an example or enter your own prompt to begin.")