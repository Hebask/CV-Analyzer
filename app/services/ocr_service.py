from typing import List
import pytesseract
from pdf2image import convert_from_bytes
from app.core.config import settings

# Use settings loaded from .env
POPPLER_BIN = settings.POPPLER_BIN
TESSERACT_CMD = settings.TESSERACT_CMD

if TESSERACT_CMD:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

def ocr_pdf_bytes(file_bytes: bytes, dpi: int = 250) -> str:
    if not POPPLER_BIN:
        raise RuntimeError("POPPLER_BIN is not set in .env (Poppler Library\\bin).")
    if not TESSERACT_CMD:
        raise RuntimeError("TESSERACT_CMD is not set in .env (path to tesseract.exe).")

    images = convert_from_bytes(
        file_bytes,
        dpi=dpi,
        poppler_path=POPPLER_BIN
    )

    texts: List[str] = []
    for img in images:
        texts.append(pytesseract.image_to_string(img, lang="eng") or "")

    return "\n".join(texts).strip()
