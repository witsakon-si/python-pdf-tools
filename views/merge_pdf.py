import streamlit as st
from PyPDF2 import PdfWriter

def create_page():
    merger = PdfWriter()

    st.title("Let's Merge PDF")

    uploaded_files = st.file_uploader(
        label="Choose a PDF file", accept_multiple_files=True, type=["pdf"]
    )

    if len(uploaded_files) < 2:
        st.write('')
    else:
        if st.button('Merge'):
            for uploaded_file in uploaded_files:
                merger.append(uploaded_file)
                merger.write("merged-pdf.pdf")
                merger.close()
            
            with open("merged-pdf.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            st.write("Complete merge. Let's Download")
            st.download_button(label="Download PDF",
                            data=PDFbyte,
                            file_name="merged-pdf.pdf",
                            mime='application/octet-stream')
    return True