import pytesseract
from pdf2image import convert_from_path
from PIL import Image, ImageEnhance, ImageFilter
from pptx import Presentation
from docx import Document
from ppt_to_pdf import ppt_to_pdf
from imageTopdf import image_to_pdf
from util import OUTPUT_PDF_PATH
import os

# Configure the path to the Tesseract executable
#pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"

def preprocess_image(image):
    # Ensure the image is in 'L' (grayscale) mode before processing
    if image.mode != 'L':
        image = image.convert('L')
    
    # Apply thresholding to convert the image to black and white
    image = image.point(lambda x: 0 if x < 140 else 255, '1')
    
    # Apply filters if necessary, e.g., sharpness, contrast
    image = image.filter(ImageFilter.MedianFilter())
    
    # Convert back to 'L' mode before enhancing contrast
    image = image.convert('L')
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)
    
    return image

# Function to extract text from an image
def extract_text_from_image(image_path):
    #image = Image.open(image_path)
    # Example usage
    output_pdf_path = OUTPUT_PDF_PATH
    image_to_pdf(image_path, output_pdf_path)
    #processed_image = preprocess_image(image)
    text = extract_text_from_pdf(output_pdf_path)
    #text = pytesseract.image_to_string(processed_image)
    return text

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""
    for image in images:
        processed_image = preprocess_image(image)
        text += pytesseract.image_to_string(processed_image)
    return text

# Function to extract text from a PowerPoint presentation
def extract_text_from_ppt(ppt_path):
    pdf_path = ppt_to_pdf(ppt_path, "output.pdf")
    text = extract_text_from_pdf(pdf_path)
    return text

# Function to extract text from a Word document
def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# Main function to handle different file types
def extract_text(file_path):
    file_ext = os.path.splitext(file_path)[1].lower()
    
    if file_ext in [".jpg", ".jpeg", ".png", ".bmp", ".gif"]:
        return extract_text_from_image(file_path)
    elif file_ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif file_ext == ".pptx":
        return extract_text_from_ppt(file_path)
    elif file_ext == ".docx":
        return extract_text_from_docx(file_path)
    else:
        return "Unsupported file format"

