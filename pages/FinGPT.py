import os
import json

import streamlit as st
import groq

# fetch GROQ_API_KEY from streamlit secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# configuring streamlit page settings
st.set_page_config(
    page_title="llama3-70b Chat",
    page_icon="💬",
    layout="centered"
)
client  = groq.Groq(api_key=GROQ_API_KEY)
# initialize chat session in streamlit if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# streamlit page title
st.title("🤖 QuantBot")

# display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# input field for user's message
user_prompt = st.chat_input("Ask QuantBot...")

if user_prompt:
    # add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # send user's message to GPT-4o and get a response
    response = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a algotrading helper named QuantBot. Provide insights on the strategies and code given and help to make it accurate"},
            *st.session_state.chat_history
        ],
        temperature=0.0,
        seed=24
    )

    assistant_response = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # display GPT-4o's response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
