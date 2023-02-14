import img2pdf
from PIL import Image
import os

pages = [1,2,3,4,5]

for page in pages:
    page_index = '000' + str(pages.index(page)+1)    

    # storing image path
    img_path = '.\input-png\page' + page_index[-3:] + '_signed.png'
    
    # storing pdf path
    pdf_path = '.\output-pdf\page' + page_index[-3:] + '_signed.pdf'
    
    # opening image
    image = Image.open(img_path)
    
    # converting into chunks using img2pdf
    pdf_bytes = img2pdf.convert(image.filename)
    
    # opening or creating pdf file
    file = open(pdf_path, "wb")
    
    # writing pdf files with chunks
    file.write(pdf_bytes)
    
    # closing image file
    image.close()
    
    # closing pdf file
    file.close()
    
    # output
    print('Successfully exported ' + pdf_path)