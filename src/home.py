# Contents of ~/my_app/streamlit_app.py
import streamlit as st

def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def openai_api_bot():
    st.markdown("# openai_api_bot ❄️")
    st.sidebar.markdown("# openai_api_bot ❄️")

page_names_to_funcs = {
    "Main Page": main_page,
    "openai_api_bot": openai_api_bot
}
