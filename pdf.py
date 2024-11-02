from PyPDF2 import PdfReader, PdfWriter

def split_pdf_by_chapters(input_pdf, chapters):
    reader = PdfReader(input_pdf)
    for idx, (start, end) in enumerate(chapters):
        writer = PdfWriter()
        for page_num in range(start - 1, end):  # Adjusting for 0-based index
            writer.add_page(reader.pages[page_num])
        with open(f"chapter_{idx + 1}.pdf", "wb") as output_pdf:
            writer.write(output_pdf)
    print("Chapters extracted as separate PDF files.")

# Example usage
input_pdf = "FluentPython2.pdf"
chapters = [
    (3, 20),     # Chapter 1: The Python Data Model
    (21, 76),    # Chapter 2: An Array of Sequences
    (77, 116),   # Chapter 3: Dictionaries and Sets
    (117, 162),  # Chapter 4: Unicode Text Versus Bytes
    (163, 200),  # Chapter 5: Data Class Builders
    (201, 230),  # Chapter 6: Object References, Mutability, and Recycling
    (231, 252),  # Chapter 7: Functions as First-Class Objects
    (253, 302),  # Chapter 8: Type Hints in Functions
    (303, 340),  # Chapter 9: Decorators and Closures
    (341, 362),  # Chapter 10: Design Patterns with First-Class Functions
    (363, 396),  # Chapter 11: A Pythonic Object
    (397, 430),  # Chapter 12: Special Methods for Sequences
    (431, 486),  # Chapter 13: Interfaces, Protocols, and ABCs
    (487, 518),  # Chapter 14: Inheritance: For Better or for Worse
    (519, 560),  # Chapter 15: More About Type Hints
    (561, 592),  # Chapter 16: Operator Overloading
    (593, 656),  # Chapter 17: Iterators, Generators, and Classic Coroutines
    (657, 694),  # Chapter 18: with, match, and else Blocks
    (695, 742),  # Chapter 19: Concurrency Models in Python
    (743, 774),  # Chapter 20: Concurrent Executors
    (775, 834),  # Chapter 21: Asynchronous Programming
    (835, 878),  # Chapter 22: Dynamic Attributes and Properties
    (879, 906),  # Chapter 23: Attribute Descriptors
    (907, 956)   # Chapter 24: Class Metaprogramming
]

split_pdf_by_chapters(input_pdf, chapters)
