from PIL import Image

def image_to_pdf(image_path, output_pdf_path):
    # Open the image
    image = Image.open(image_path)
    
    # Convert the image to RGB mode if it's not already in RGB mode
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Save the image as a PDF
    image.save(output_pdf_path, "PDF", resolution=100.0)
    
    print(f"Image has been successfully converted to PDF and saved as {output_pdf_path}")

