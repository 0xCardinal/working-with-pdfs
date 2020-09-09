# Apply page numbers to all the page of the PDF!
# Author: Kumar Ashwin

import os,sys
try:
    from PyPDF2 import PdfFileWriter, PdfFileReader
    import io
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
except ImportError:
    os.system("pip install reportlab")
    os.system("pip install PyPDF2")
    print("=======================================")
    print("Dependencies installed! Please re-run the script!")
    sys.exit(1)

try:
    path =  sys.argv[1] # path of file
    out_path = sys.argv[2] # path of output file
    existingPDF = PdfFileReader(open(path,"rb+"))
except:
    help = """Apply page numbers to all the page of the PDF!
Page Style: A4

Usage:
======
python3 apply-page-number.py <path of  original file> <path of the new file>

Example:
========
python3 apply-page-numbers.py ./original.pdf ./dest/destination.pdf
"""
    print(help)
    sys.exit(2)

packet = io.BytesIO()
newCanvas = canvas.Canvas(packet, pagesize=A4)

# Creates a new pdf for page numbers
for i in range(1,existingPDF.getNumPages()+1):
    pageNum = newCanvas.getPageNumber()
    newCanvas.drawString(530, 40, str(i))
    newCanvas.showPage()
newCanvas.save()

packet.seek(0)
newPDF = PdfFileReader(packet)
output = PdfFileWriter()

# Merges two PDFs into one
for i in range(0, existingPDF.getNumPages()):
    page = existingPDF.getPage(i)
    page.mergePage(newPDF.getPage(i))
    output.addPage(page)

outputStream = open(out_path, "wb")
output.write(outputStream)
outputStream.close()