import PyPDF2
import sys
from typing import Union, Literal, List

# inputs = sys.argv[1:]
#
# # with open("dummy.pdf", "rb") as file:
# #     reader = PyPDF2.PdfReader(file)
# #     page = reader.pages[0]
# #     page.rotate(180)
# #     writer = PyPDF2.PdfWriter()
# #     writer.add_page(page)
# #     with open("tilt.pdf", "wb") as new_file:
# #         writer.write(new_file)
#
# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfMerger()
#     for pdf in pdf_list:
#         merger.append(pdf)
#     merger.write("super.pdf")
#
#
# pdf_combiner(inputs)

content_pdf = PyPDF2.PdfReader(open("super.pdf", "rb"))
watermark = PyPDF2.PdfReader(open("wtr.pdf", "rb"))
output = PyPDF2.PdfWriter()

for i in range(len(content_pdf.pages)):
    page = content_pdf.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

with open("watermarked_output.pdf", "wb") as outputFile:
    output.write(outputFile)
