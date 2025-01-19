import fitz  # PyMuPDF

def extract_text_from_pdf(content: bytes, max_pages: int = 10) -> str:
    pdf_document = fitz.open(stream=content, filetype="pdf")
    text = ""
    for page_num in range(min(pdf_document.page_count, max_pages)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text