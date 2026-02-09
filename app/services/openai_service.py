from datetime import datetime, timezone
from typing import Any, Dict
from openai import OpenAI

from app.core.config import settings
from app.schemas.cv_analysis_schema import CV_ANALYSIS_JSON_SCHEMA

client = OpenAI(api_key=settings.OPENAI_API_KEY)

DEFAULT_MODEL = "gpt-4o-mini"  # keep your chosen model

def build_system_prompt(requirements: Dict[str, Any]) -> str:
    return (
        "You are a strict CV analyzer.\n"
        "Return output that matches the provided JSON schema exactly.\n"
        "Use English only.\n"
        "Do not invent facts. If missing, use empty string/empty array, or 0 for years_experience.\n"
        "All scores must be integers 0-100.\n"
        "Ensure overall_score is consistent with dimension_scores.\n"
        f"REQUIREMENTS_JSON:\n{requirements}\n"
    )

def analyze_cv_text(cv_text: str, requirements: Dict[str, Any], model: str = DEFAULT_MODEL) -> Dict[str, Any]:
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": build_system_prompt(requirements)},
            {"role": "user", "content": f"CV_TEXT:\n{cv_text}"}
        ],
        response_format={
            "type": "json_schema",
            "json_schema": CV_ANALYSIS_JSON_SCHEMA
        }
    )

    data = resp.choices[0].message.content

    import json
    obj = json.loads(data)

    obj["meta"]["model"] = obj["meta"].get("model") or model
    obj["meta"]["analysis_timestamp_utc"] = obj["meta"].get("analysis_timestamp_utc") or datetime.now(timezone.utc).isoformat()
    obj["meta"]["requirements_version"] = obj["meta"].get("requirements_version") or "v1"

    return obj
