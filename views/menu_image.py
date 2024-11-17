from streamlit_option_menu import option_menu
from views import crop_image, convert_image

def create_page():
    selected = option_menu(None, ["Crop", "Convert"],
            icons=['crop', 'bi-floppy-fill'], default_index=0, orientation="horizontal")

    if selected == "Crop":
        crop_image.create_page()
    elif selected == "Convert":
        convert_image.create_page()
