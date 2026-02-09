import os
from typing import List
import pytesseract
from pdf2image import convert_from_bytes

TESSERACT_CMD = os.getenv("TESSERACT_CMD")
POPPLER_BIN = os.getenv("POPPLER_BIN")

if TESSERACT_CMD:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

def ocr_pdf_bytes(file_bytes: bytes, dpi: int = 250) -> str:
    images = convert_from_bytes(
        file_bytes,
        dpi=dpi,
        poppler_path=POPPLER_BIN
    )

    texts: List[str] = []
    for img in images:
        texts.append(pytesseract.image_to_string(img, lang="eng") or "")

    return "\n".join(texts).strip()
