from datetime import datetime, timezone
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.core.db import get_db
from app.services.pdf_service import extract_pdf_text_with_fallback

router = APIRouter(prefix="/cv", tags=["cv"])

@router.post("/upload")
async def upload_cv(
    user_id: str = Form(...),
    file: UploadFile = File(...)
):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    file_bytes = await file.read()
    if not file_bytes:
        raise HTTPException(status_code=400, detail="Empty file.")

    try:
        text, source = extract_pdf_text_with_fallback(file_bytes)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"PDF extraction failed: {e}")

    if len(text) < 50:
        raise HTTPException(
            status_code=400,
            detail="Extracted text is too small even after OCR. PDF may be corrupted or unreadable."
        )

    db = get_db()
    col = db["cv_uploads"]

    doc = {
        "user_id": user_id,
        "filename": file.filename,
        "uploaded_at": datetime.now(timezone.utc).isoformat(),
        "text": text,
        "text_length": len(text),
        "text_source": source,
        "status": "uploaded"
    }

    inserted = col.insert_one(doc)

    return {
        "id": str(inserted.inserted_id),
        "text_source": source,
        "extracted_chars": len(text),
        "extracted_preview": text[:600]
    }
