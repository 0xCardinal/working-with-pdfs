# Merge two PDFs together!
# Author: Kumar Ashwin

import os,sys
try:
    from PyPDF2 import PdfFileWriter, PdfFileReader
except ImportError:
    os.system("pip install PyPDF2")
    print("=======================================")
    print("Dependencies installed! Please re-run the script!")
    sys.exit(1)

try:
    path1 =  sys.argv[1]     # path of file 1
    path2 =  sys.argv[2]     # path of file 2
    out_path = sys.argv[3]  # path of output file
    pdf1 = PdfFileReader(open(path1,"rb"))
    pdf2 = PdfFileReader(open(path2,"rb+"))
except:
    help = """Merge two PDF files! First PDF on top of the second PDF!
Page Style: A4

Usage:
======
python3 merge-pdf.py <path of 1st file> <path for 2nd file> <path for output file>

Example:
========
python3 merge-pdf.py ./index.pdf ./original.pdf ./dest/destination.pdf

Add the index on top of original PDF file.
"""
    print(help)
    sys.exit(2)

pdfWriter = PdfFileWriter()

# PDF 1 iterator
for pageNum in range(pdf1.numPages):
    pageObj = pdf1.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# PDF 2 iterator
for pageNum in range(pdf2.numPages):
    pageObj = pdf2.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# Merging
output = open(out_path,"wb")
pdfWriter.write(output)

output.close()