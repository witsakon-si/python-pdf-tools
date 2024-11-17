import streamlit as st
from io import BytesIO
from PIL import Image

def create_page():

    st.title("Let's Convert Image")

    uploaded_file = st.file_uploader(
        label="Choose a Image file", accept_multiple_files=False, type=["png", "jpg"]
    )

    if uploaded_file:
        aspect_choice = st.radio(
            "Select image size",
            ["16x16", "32x32", "48x48", "64x64", "128x128", "256x256", "Original"],
            index=6, horizontal=True
        )
        aspect_dict = {
            "16x16": (16, 16),
            "32x32": (32, 32),
            "48x48": (48, 48),
            "64x64": (64, 64),
            "128x128": (128, 128),
            "256x256": (256, 256),
            "Original": None
        }

        file_name = "convert-" + uploaded_file.name
        file_name = file_name.replace(".png", "")
        file_name = file_name.replace(".jpg", "")
        file_name = file_name.replace(".jpeg", "")

        image = Image.open(uploaded_file)
        new_image = image
        if aspect_dict[aspect_choice] is not None:
            new_image = image.resize(aspect_dict[aspect_choice])

        # PNG
        buf_png = BytesIO()
        new_image.save(buf_png, format='PNG')
        byte_png = buf_png.getvalue()
        st.download_button(label="Download (PNG)", data=byte_png, file_name=file_name+'.png', mime="image/png")
        # JPEG
        buf_jpg = BytesIO()
        rgb_im = new_image.convert('RGB')
        rgb_im.save(buf_jpg, format='JPEG')
        byte_jpg = buf_jpg.getvalue()
        st.download_button(label="Download (JPEG)", data=byte_jpg, file_name=file_name+'.jpg', mime="image/jpg")
        # ICON
        buf_icon = BytesIO()
        new_image.save(buf_icon, format='ICO')
        byte_icon = buf_icon.getvalue()
        st.download_button(label="Download (ICO)", data=byte_icon, file_name=file_name+'.ico', mime="image/icon")

        st.subheader('Preview')
        st.image(new_image)

