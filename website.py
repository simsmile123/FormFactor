import streamlit as st

st.set_page_config(
    page_title="Form Factor",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("Form Factor")
st.write("Path to Perfection")
st.divider()
st.write("")
st.subheader("Video Upload")
input_video = st.file_uploader("Choose a video: ", type=["mp4"])