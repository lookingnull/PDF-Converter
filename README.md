# PDF-Converter

A Python script is utilized for converting PDF files into PNG format, with the purpose of merging multiple PDF files into one.

To use the script, the user must first modify the folder path in pdf_convert.py to point to the directory containing the PDF files. Once this is done, the script can be executed. However, it is important to note that the script will delete the original PDF files once the conversion process is complete. It is strongly advised that users ensure they have a backup of all PDF files before executing the script, as the files will be permanently deleted otherwise. 

****** This too and information is provided for educational purposes only.


The following dependencies must be installed for the script to function properly: libpng-dev, libjpeg-dev, and zlib1g-dev. Additionally, the pdf2image package must be installed via pip, while the poppler-utils package can be installed using the sudo apt-get command.

1. Install dependencies: sudo apt-get install libpng-dev libjpeg-dev zlib1g-dev

2. Install pdf2image: pip install pdf2image

3. Install poppler: sudo apt-get install poppler-utils

4. Open the pdf_convert.py file, edit the folder path so that it points to the directory that containts all the PDF files. Run the python script.

****** WARNING**************

This script will delete the PDF files once the conversion is completed. Make sure you have a backup of all the PDF files. Otherwise, they will be GONE!!!

****** WARNING**************


Use at your own risk. I am not responsible for improper use of this tool. 
