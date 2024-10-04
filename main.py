import streamlit as st
from streamlit_option_menu import option_menu
from views import menu_pdf, menu_image, about_me

with st.sidebar:
    selected = option_menu("PDF/Image Tools", ["PDF", "Image", "About Me"], 
        icons=['file-earmark-pdf-fill', 'image-fill', 'question-diamond-fill'], menu_icon="tools", default_index=0)

if selected == "PDF":
    menu_pdf.create_page()
elif selected == "Image":
    menu_image.create_page()
else:
    about_me.create_page()
