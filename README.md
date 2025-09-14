📊 Market Trends Chatbot (Streamlit + Gemini API)

An interactive chatbot built with Streamlit and Google Gemini API that provides insights on market trends using a custom context file.
This project demonstrates how to integrate LLMs with business-specific knowledge for context-aware Q&A.

✨ Features

✅ Loads context data from market_context.txt

✅ Simple Streamlit UI for asking questions

✅ Uses Google Gemini-2.5-Flash for fast and professional answers

✅ Customizable context → just update market_context.txt

✅ Error handling for missing files & invalid inputs

🚀 Installation & Setup

Clone this repository

git clone https://github.com/your-username/market-trends-chatbot.git
cd market-trends-chatbot


Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # for Linux/Mac
venv\Scripts\activate      # for Windows


Install dependencies

pip install -r requirements.txt


Example requirements.txt:

streamlit
google-generativeai


Set your Gemini API key
Open the code and replace:

GEMINI_API_KEY = "your_gemini_api_key_here"


Or, set it as an environment variable:

export GEMINI_API_KEY="your_api_key"


Add your context file
Create a file named market_context.txt with background info, reports, or data about market trends.

▶️ Usage

Run the Streamlit app:

streamlit run app.py


Enter your question in the text box

The chatbot will generate a professional answer based on your context file
