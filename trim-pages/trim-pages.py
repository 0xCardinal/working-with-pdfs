# Trim pages from the PDF!
# Author: Diksha Choudhary and Kumar Ashwin

import os,sys
try:
    from PyPDF2 import PdfFileWriter, PdfFileReader
except ImportError:
    os.system("pip install PyPDF2")
    print("=======================================")
    print("Dependencies installed! Please re-run the script!")
    sys.exit(1)

try:
    path =  sys.argv[1]     # path of file
    start = int(sys.argv[2])     # starting page number
    end = int(sys.argv[3])   #ending page number
    out_path = sys.argv[4]  # path of output file
    existingPDF = PdfFileReader(open(path,"rb+"))
except:
    help = """Trim pages from the PDF!
Page Style: A4

Usage:
======
python3 trim-pages.py <path of  original file> <start page number to be removed> <end page number to be removed> <path of the new file>

Example:
========
python3 trim-pages.py ./original.pdf 0 5 ./dest/destination.pdf

The above script will remove first 5 pages from the PDF.
"""
    print(help)
    sys.exit(2)

pdfWriter = PdfFileWriter()

for page in range(existingPDF.numPages):
  pageObj = existingPDF.getPage(page)
  if(page < start-1 or page > end-1):
      pdfWriter.addPage(pageObj)

outputStream = open(out_path,"wb")
pdfWriter.write(outputStream)
outputStream.close()