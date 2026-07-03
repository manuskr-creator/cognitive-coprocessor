import streamlit as st
import google.generativeai as genai
import os

# Retrieve the API key from Streamlit's secret management
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

st.write("Step 2: API connection configured successfully!")