import streamlit as st

def generate_code(prompt):
    # Replace this with your Hugging Face function
    return f"Generated Code for: {prompt}"

st.title("Code Assistant")
user_input = st.text_input("Enter your coding prompt")
if st.button("Generate"):
    st.write(generate_code(user_input))
