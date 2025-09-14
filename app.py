import streamlit as st
import google.generativeai as genai


GEMINI_API_KEY = "your_gemini_api_key_here"

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Load context file
def load_context(file_path="market_context.txt"):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "No context file found. Please add market_context.txt."

# Streamlit UI
st.title(" Market Trends Chatbot")

context_data = load_context()

st.subheader("Ask about market trends")
user_query = st.text_input("Your Question:")

if st.button("Get Answer"):
    if not user_query.strip():
        st.warning("Please enter a question.")
    else:
        # Build prompt
        prompt = f"""You are an expert in market trends. Use the given context to answer.

Context:
{context_data}

User Question:
{user_query}

Answer in a clear and professional way:
"""

        try:
            model = genai.GenerativeModel("gemini-2.5-flash")
            response = model.generate_content(prompt)
            st.write(" Chatbot Answer:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
