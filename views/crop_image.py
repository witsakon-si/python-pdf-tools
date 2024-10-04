import streamlit as st
from io import BytesIO
from pathlib import Path
from streamlit_cropper import st_cropper
from PIL import Image

def create_page():

    st.title("Let's Crop Image")
    
    uploaded_file = st.file_uploader(
        label="Choose a Image file", accept_multiple_files=False, type=["png", "jpg"]
    )

    if uploaded_file:
        aspect_choice = st.radio(label="Aspect Ratio", options=["1:1", "16:9", "4:3", "2:3", "Free"], horizontal=True)
        aspect_dict = {
            "1:1": (1, 1),
            "16:9": (16, 9),
            "4:3": (4, 3),
            "2:3": (2, 3),
            "Free": None
        }
        aspect_ratio = aspect_dict[aspect_choice]
        img = Image.open(uploaded_file)
        cropped_img = st_cropper(img, realtime_update=True, box_color='#ff5436', aspect_ratio=aspect_ratio)
        
        img_format = "PNG" if Path(uploaded_file.name).suffix == '.png' else "JPEG"
        img_mine = "image/png" if Path(uploaded_file.name).suffix == '.png' else "image/jpg"

        if cropped_img:
            # original image type
            buf = BytesIO()
            cropped_img.save(buf, format=img_format)
            byte_im = buf.getvalue()
            file_name = "crop-" + uploaded_file.name
            
            # wepb
            buf_wepb = BytesIO()
            cropped_img.save(buf_wepb, format="webp", optimize=True, quality=80)
            byte_wepb = buf_wepb.getvalue()
            file_name_wepb = "crop-" + uploaded_file.name + ".wepb"
            file_name_wepb = file_name_wepb.replace(".png", "")
            file_name_wepb = file_name_wepb.replace(".jpg", "")
            file_name_wepb = file_name_wepb.replace(".jpeg", "")
            
            
            st.download_button(label="Download (Original Type)", data=byte_im, file_name=file_name, mime=img_mine)
            st.download_button(label="Download (.wepb)", data=byte_wepb, file_name=file_name_wepb, mime="image/webp")
        