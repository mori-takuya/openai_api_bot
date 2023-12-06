from openai import OpenAI
import streamlit as st

st.title("Chatもどき")
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "プログラムの手伝いをする"}]

#for msg in st.session_state.messages:
#    st.chat_message(msg.role).write(msg.content)

if prompt := st.chat_input():
    client = OpenAI(
      api_key=st.secrets.OpenAIAPI.openai_api_key
    )
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
