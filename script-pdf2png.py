from pdf2image import convert_from_path
pages = convert_from_path('.\input-pdf\INPUT.pdf', 500)
for page in pages:
    page_index = '000' + str(pages.index(page)+1)    
    page.save('.\output-png\page' + page_index[-3:] + '.png', 'PNG')