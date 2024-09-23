import streamlit as st

def create_page():

    st.subheader("About Me  " + ":coffee:", divider=True)
    code = '''def aboutMe():
    print("I'm Witsakon Siangwithan")
    print("I love coding and learning new tech stacks")
    print("Email: witsakon.si@gmail.com")
    print("GitHub: https://github.com/witsakon-si")
    '''
    st.code(code, language="python")
    