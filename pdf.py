from PyPDF2 import PdfReader, PdfWriter

def split_pdf_by_chapters(input_pdf, chapters):
    reader = PdfReader(input_pdf)
    for idx, (start, end) in enumerate(chapters):
        writer = PdfWriter()
        for page_num in range(start, end + 1):
            writer.add_page(reader.pages[page_num - 1])  # Adjusting for 0-based index
        with open(f"chapter_{idx + 1}.pdf", "wb") as output_pdf:
            writer.write(output_pdf)
    print("Chapters extracted as separate PDF files.")

# Example usage
input_pdf = "FluentPython.pdf"
chapters = [
    (1, 50),  # Chapter 1: pages 1-15
    
    # Add more chapters here as (start_page, end_page)
]
split_pdf_by_chapters(input_pdf, chapters)
