from PyPDF2 import PdfMerger

pages = [1,2,3,4,5]

merger = PdfMerger()

for page in pages:
    page_index = '000' + str(pages.index(page)+1)    
    pdf_path = '.\output-pdf\page' + page_index[-3:] + '_signed.pdf'
    merger.append(pdf_path)

merger.write('.\OUTPUT.pdf')
merger.close()