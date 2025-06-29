# We have to merge multiple pdfs into one using python open-source module pypdf
from pypdf import PdfWriter, PdfReader

merger = PdfWriter()
pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']

for pdf_file in pdf_files:
    reader = PdfReader(pdf_file)
    merger.append(reader)

merger.write("merged_output.pdf")
merger.close()