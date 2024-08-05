import streamlit as st
from io import StringIO

# TODO: Give a header, way to upload resume, then go to a separate page with the chat.
# TODO: once chat is finished (user will click a button), score it and go to another page
# TODO: with a score

st.header("LLM Interview Prep", divider=True)

st.write("An LLM app to do mock interview prep based on your resume. Upload a your resume to get started!")

uploaded_file = st.file_uploader(
    "Resume", type=["pdf", "txt", "doc", "docx"], )

# OK, so basically just need to go to the chat screen after we process it.
# need ot craft the prompts in the notebooks


def on_click_continue():
    """
    Save resume & go to next page
    """
    st.session_state['resume'] = uploaded_file
    # TODO: Go to next page
    return


st.button(
    "Continue",
    on_click=on_click_continue,
    disabled=uploaded_file is None
)
