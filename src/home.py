# Contents of ~/my_app/streamlit_app.py
import streamlit as st

def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def page2():
    st.markdown("# app ❄️")
    st.sidebar.markdown("# app ❄️")

page_names_to_funcs = {
    "Main Page": main_page,
    "app": app
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
