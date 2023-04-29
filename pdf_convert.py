import os
import glob
import PyPDF2
import time
from pdf2image import convert_from_path

# Define the folder containing the PDF files. 
folder_path = r"/<path to pdf files>"

# Use glob to find all the PDF files in the folder
pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))

# Loop through each PDF file
for pdf_file in pdf_files:
    try:
        # Use pdf2image to convert each page of the PDF file to an image
        pages = convert_from_path(pdf_file)

        # Loop through each image and save it to a file
        for i, page in enumerate(pages):
            image_file_path = os.path.join(folder_path, f"{os.path.basename(pdf_file)}_page{i+1}.png")
            page.save(image_file_path, "PNG")

        # Delete the PDF file
        # ****************WARNING!!!!!! YOUR ORIGINAL PDF FILE WILL BE DELETED. MAKE SURE TO HAVE A BACKUP******************
       # os.remove(pdf_file) old method
        pdf_file_path = os.path.abspath(pdf_file)
        os.remove(pdf_file_path)

        # Wait for 4 seconds this will allow pc to catch up 
        time.sleep(4)
        
        
    except Exception as e:
        print(f"Error converting PDF file '{pdf_file}': {e}")
