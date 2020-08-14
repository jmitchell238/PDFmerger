"""PDF Merger Project

This Python program is designed to receive multiple PDF files from the
user and output a single PDF file.

Example:
    The following code placed into the Terminal will produce one single file
    called outputfile.pdf. It will combine all the files entered before it in
    the order that the user specified them::

        $ python3 PDFmerger.py file1.pdf file2.pdf file3.pdf outputfile.pdf

Input:
    However many PDF files the user wants to combine into one PDF file.

Output:
    1 PDF file.

Execute:
    Run a variation of the following line in the Console Terminal.
        $ python3 PDFmerger.py file1.pdf file2.pdf file3.pdf outputfile.pdf

"""

import PyPDF2
import sys

inputs = sys.argv[1:-1]
output = sys.argv[-1]

def pdf_combine(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output)

pdf_combine(inputs)