import streamlit as st
import tempfile
import shutil
import os
from extraction import extract_text
from util import DEFAULT_TEXT

# Set page title and logo
st.set_page_config(page_title="Text Extractor", page_icon="💬")

# Add title and logo
st.title("Text Extractor")
st.sidebar.image(
    "logo.jpg", use_column_width=False, width=150
)  # Make sure you have a logo.jpg file in the same directory


def download_file(translated_text, filename):
    st.download_button(
        label="Download file",
        data=translated_text,
        file_name=filename,
        mime="text/plain",
    )


text_container = st.container(height=250, border=True)
extracted_text = DEFAULT_TEXT

# File uploader
uploaded_file = st.file_uploader(
    "Choose a file (Image/PDF/PPT)", type=["jpg", "png", "pdf", "pptx"]
)

if uploaded_file is not None:
    # Save the uploaded file to a temporary directory
    with tempfile.NamedTemporaryFile(
        delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}"
    ) as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        temp_file_path = temp_file.name

    # Extract text from the temporary file
    extracted_text = extract_text(temp_file_path)
    output_filename = f"{uploaded_file.name.split('.')[0]}.txt"
    download_file(extracted_text, output_filename)

    # Clean up temporary file
    os.remove(temp_file_path)

with text_container:
    st.write(extracted_text)
