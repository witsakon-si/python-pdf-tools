import streamlit as st
from pdf2image import convert_from_path
from streamlit_cropper import st_cropper
from PIL import Image
from PyPDF2 import PdfWriter, PdfReader

def create_page():

    st.title("Let's Crop PDF")

    uploaded_file = st.file_uploader(
        label="Choose a PDF file", accept_multiple_files=False, type=["pdf"]
    )
    if uploaded_file:
        pdf_reader = PdfReader(uploaded_file.name)
        pdf0 = pdf_reader.pages[0]
        pdf_box = pdf0.mediabox
        
        images = convert_from_path(uploaded_file.name)
        for i, image in enumerate(images):
            image.thumbnail((pdf_box.width, pdf_box.height))
            image.save(f'page{i}.jpg', 'JPEG')
        img = Image.open("page0.jpg")
        box = st_cropper(img, realtime_update=True, box_color='#000000', return_type='box', aspect_ratio=None)

        if len(images) < 1:
            st.write('')
        else:
            if st.button('Crop'):
                reader = PdfReader(uploaded_file.name)
                writer = PdfWriter()
                page0 = reader.pages[0]
                
                x, y, w, h = (box['left'], box['top'], box['width'], box['height'])
                upper_left = page0.cropbox.upper_left
                page_x, page_y = upper_left[0], upper_left[1]
                old_upper_left = [page_x.as_numeric(), page_y.as_numeric()]
                new_upper_left  = (old_upper_left[0] + x, old_upper_left[1] - y)
                new_lower_right = (new_upper_left[0] + w, new_upper_left[1] - h)
                page0.cropbox.upper_left  = new_upper_left
                page0.cropbox.lower_right = new_lower_right
                
                writer.add_page(page0)
                writer.write("crop-pdf.pdf")
                writer.close()

                with open("crop-pdf.pdf", "rb") as pdf_file:    
                    PDFbyte = pdf_file.read()
                st.write("Complete crop. Let's Download")
                st.download_button(label="Download PDF", data=PDFbyte, file_name="crop-pdf.pdf", mime='application/octet-stream')
        return True