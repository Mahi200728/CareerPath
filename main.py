import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import google.generativeai as genai


# Load environment variables
load_dotenv()

# Configure generative AI with Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit UI
st.title("Career Path Finder (Powered by AI)")
st.write("Find your ideal career path based on your interests and skills, enhanced by AI!")

# Input user preferences
st.subheader("Step 1: What's your area of interest?")
interest = st.selectbox("Choose an area:", ["Science", "Technology", "Arts", "Business", "Healthcare"])

st.subheader("Step 2: What's your key strength or skill?")
skill = st.selectbox("Choose your top skill:", ["Problem-solving", "Creativity", "Technical", "Empathy", "Leadership"])

# Define function to query Google Gemini
def get_career_recommendations_gemini(interest, skill):
    prompt = (
        f"I am interested in the {interest} field and my key strength is {skill}. "
        "Suggest potential career paths for me with a brief explanation of each."
    )
    try:
        # Generating response using Gemini API
        model = genai.GenerativeModel("gemini-1.5-flash-8b") 
        response = model.generate_content([prompt])  
        
        # Return the response content, if available
        if response and hasattr(response, 'text'):
            return response.text.strip()  
        else:
            return "No response generated from AI."
    except Exception as e:
        return f"Error connecting to Google Gemini: {e}"

# Output AI-driven career suggestions
if st.button("Find Careers with AI"):
    with st.spinner("Analyzing your interests and skills..."):
        ai_recommendations = get_career_recommendations_gemini(interest, skill)
        st.write("### AI-Powered Career Recommendations:")
        st.write(ai_recommendations)

st.write("Leverage AI and keep exploring your unique strengths!")
