import streamlit as st
from extraction import extract_text
from util import DEFAULT_TEXT

# Set page title and logo
st.set_page_config(page_title="Text Extractor", page_icon="💬")

# Add title and logo
st.title("Text Extractor")
st.sidebar.image("logo.jpg", use_column_width=False, width=150) # Make sure you have a logo.png file in the same directory

def download_file(translated_text,filename):
            st.download_button(
                label="Download file",
                data=translated_text,
                file_name= filename,
                mime="text/plain"
            )

text_container = st.container(border=True, height=250)
extracted_text = DEFAULT_TEXT

# File uploader
uploaded_file = st.file_uploader("Choose a file (Image/PDF/PPT)", type=["jpg", "png", "pdf", "pptx"])

if uploaded_file is not None:
    filename = uploaded_file.name
    extracted_text = extract_text(filename)
    filename = f"output/{filename.split('.')[0]}.txt"
    download_file(extracted_text,filename)

    
with text_container: 
       st.write(extracted_text)