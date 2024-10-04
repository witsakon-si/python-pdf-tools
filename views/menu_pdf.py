from streamlit_option_menu import option_menu
from views import merge_pdf, crop_pdf

def create_page():
    selected = option_menu(None, ["Merge", "Crop"], 
            icons=['file-earmark-plus-fill', 'crop'], default_index=0, orientation="horizontal")

    if selected == "Merge":
        merge_pdf.create_page()
    elif selected == "Crop":
        crop_pdf.create_page()