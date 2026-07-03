import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.write("--- Available Models ---")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        st.write(model.name)
