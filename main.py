import streamlit as st
from streamlit_option_menu import option_menu
from views import merge_pdf, crop_pdf, about_me

with st.sidebar:
    selected = option_menu("PDF Tools", ["Merge", "Crop", 'About Me'], 
        icons=['file-earmark-plus-fill', 'crop', 'question-diamond-fill'], menu_icon="file-earmark-pdf-fill", default_index=0)

if selected == "Merge":
    merge_pdf.create_page()
elif selected == "Crop":
    crop_pdf.create_page()
else:
    about_me.create_page()
