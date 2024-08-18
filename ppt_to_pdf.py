import os
import comtypes.client

def ppt_to_pdf(input_file, output_file=None):
    """
    Converts a PowerPoint file to PDF.
    
    :param input_file: Path to the input PowerPoint file (.ppt or .pptx).
    :param output_file: Path to save the output PDF file. If None, saves in the same location as the input file with a .pdf extension.
    """
    # Check if the input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"The file {input_file} does not exist.")
    
    # Set the output file path
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + ".pdf"
    
    # Create a PowerPoint application object
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1

    # Open the PowerPoint file
    presentation = powerpoint.Presentations.Open(input_file)

    # Save as PDF
    presentation.SaveAs(output_file, FileFormat=32)

    # Close the presentation
    presentation.Close()

    # Quit PowerPoint application
    powerpoint.Quit()
    
    return output_file


