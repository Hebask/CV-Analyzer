from pydantic import BaseModel
from typing import Any, Dict, Optional

class AnalyzeRequest(BaseModel):
    cv_id: str
    requirements: Optional[Dict[str, Any]] = None
