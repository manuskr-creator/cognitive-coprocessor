import streamlit as st
import google.generativeai as genai

# Setup API
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Use the short name 'gemini-1.5-flash'
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("Cognitive Coprocessor")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("How can I help you?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        # Get AI response
        response = model.generate_content(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"An error occurred: {e}")
