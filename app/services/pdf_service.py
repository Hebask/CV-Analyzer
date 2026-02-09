import io
from pypdf import PdfReader
from app.services.ocr_service import ocr_pdf_bytes

MIN_TEXT_CHARS_BEFORE_OCR = 200 

def extract_pdf_text_with_fallback(file_bytes: bytes) -> tuple[str, str]:
    reader = PdfReader(io.BytesIO(file_bytes))
    pages_text = []
    for page in reader.pages:
        pages_text.append(page.extract_text() or "")
    text = "\n".join(pages_text).strip()

    if len(text) >= MIN_TEXT_CHARS_BEFORE_OCR:
        return text, "pypdf"

    ocr_text = ocr_pdf_bytes(file_bytes)
    if len(ocr_text) > len(text):
        return ocr_text, "ocr"

    return text, "pypdf"
