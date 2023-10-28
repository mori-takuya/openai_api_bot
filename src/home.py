# Contents of ~/my_app/streamlit_app.py
import streamlit as st

def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def app():
    st.markdown("# app ❄️")
    st.sidebar.markdown("# app ❄️")

page_names_to_funcs = {
    "Main Page": main_page,
    "app": app
}
