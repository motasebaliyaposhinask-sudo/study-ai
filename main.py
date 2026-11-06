import google.generativeai as genai
import streamlit as st

st.set_page_config(page_title="Study AI", layout="centered")
st.title("📚 Study AI")
st.subheader("Your Personal AI Tutor")

# API Key configuration
api_key = st.text_input("🔑 Enter Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    # Using gemini-2.5-flash for general text Q&A
    model = genai.GenerativeModel("gemini-2.5-flash")

    # User query input
    user_question = st.text_area(
        "Ask a difficult question:",
        placeholder="E.g., Explain the theory of relativity in simple terms.",
    )

    if st.button("Generate Answer"):
        if user_question:
            try:
                with st.spinner("Thinking..."):
                    response = model.generate_content(user_question)

                    st.markdown("### Answer:")
                    st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a question first.")
else:
    st.info("Please enter your Gemini API Key to continue.")
