"""DAY 22 OF 100DAYS 
PYTHON PROJECT"""
from pypdf import PdfReader,PdfWriter
reader = PdfReader("extensions.pdf")
writer = PdfWriter()

writer.append(reader)
writer.encrypt("12345")

with open("protected.pdf","wb") as file:
    writer.write(file)