from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.core.db import get_db
from app.services.openai_service import analyze_cv_text
from app.schemas.analyze import AnalyzeRequest

router = APIRouter(prefix="/cv", tags=["cv"])

@router.post("/analyze")
def analyze_cv(req: AnalyzeRequest):
    db = get_db()
    uploads = db["cv_uploads"]
    analyses = db["cv_analyses"]

    # Load CV
    try:
        doc = uploads.find_one({"_id": ObjectId(req.cv_id)})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid cv_id.")
    if not doc:
        raise HTTPException(status_code=404, detail="CV not found.")

    cv_text = doc.get("text", "")
    if len(cv_text) < 50:
        raise HTTPException(status_code=400, detail="Stored CV text is too small.")

    # Default requirements
    requirements = req.requirements or {
        "role": "General",
        "must_have": [],
        "nice_to_have": [],
        "weights": {
            "relevance_to_role": 0.25,
            "skills_match": 0.25,
            "experience_strength": 0.25,
            "education_fit": 0.15,
            "clarity_and_structure": 0.10
        }
    }

    analysis = analyze_cv_text(cv_text=cv_text, requirements=requirements)
    overall = int(analysis.get("scoring", {}).get("overall_score", 0))

    inserted = analyses.insert_one({
        "cv_upload_id": doc["_id"],
        "user_id": doc.get("user_id"),
        "filename": doc.get("filename"),
        "requirements": requirements,
        "analysis_json": analysis,
        "overall_score": overall,
        "status": "completed"
    })

    return {
        "analysis_id": str(inserted.inserted_id),
        "cv_id": req.cv_id,
        "overall_score": overall,
        "analysis": analysis
    }
