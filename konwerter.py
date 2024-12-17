from pdf2docx import Converter
pdf_file='proba.pdf'
docx_file='proba.docx'
cv=Converter(pdf_file)
cv.convert(docx_file)
cv.close()
