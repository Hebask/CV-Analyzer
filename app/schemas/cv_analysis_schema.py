CV_ANALYSIS_JSON_SCHEMA = {
    "name": "cv_analysis",
    "schema": {
        "type": "object",
        "additionalProperties": False,
        "required": [
            "candidate",
            "summary",
            "skills",
            "experience",
            "education",
            "projects",
            "certifications",
            "scoring",
            "meta"
        ],
        "properties": {
            "candidate": {
                "type": "object",
                "additionalProperties": False,
                "required": ["full_name", "email", "phone", "location", "links"],
                "properties": {
                    "full_name": {"type": "string"},
                    "email": {"type": "string"},
                    "phone": {"type": "string"},
                    "location": {"type": "string"},
                    "links": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": ["linkedin", "github", "portfolio"],
                        "properties": {
                            "linkedin": {"type": "string"},
                            "github": {"type": "string"},
                            "portfolio": {"type": "string"}
                        }
                    }
                }
            },
            "summary": {
                "type": "object",
                "additionalProperties": False,
                "required": ["headline", "years_experience", "current_title", "core_domain"],
                "properties": {
                    "headline": {"type": "string"},
                    "years_experience": {"type": "integer"},
                    "current_title": {"type": "string"},
                    "core_domain": {"type": "string"}
                }
            },
            "skills": {
                "type": "object",
                "additionalProperties": False,
                "required": ["hard_skills", "soft_skills", "tools", "languages"],
                "properties": {
                    "hard_skills": {"type": "array", "items": {"type": "string"}},
                    "soft_skills": {"type": "array", "items": {"type": "string"}},
                    "tools": {"type": "array", "items": {"type": "string"}},
                    "languages": {"type": "array", "items": {"type": "string"}}
                }
            },
            "experience": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["company", "title", "start_date", "end_date", "location", "highlights", "keywords_found"],
                    "properties": {
                        "company": {"type": "string"},
                        "title": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                        "location": {"type": "string"},
                        "highlights": {"type": "array", "items": {"type": "string"}},
                        "keywords_found": {"type": "array", "items": {"type": "string"}}
                    }
                }
            },
            "education": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["institution", "degree", "field", "start_date", "end_date", "gpa", "notes"],
                    "properties": {
                        "institution": {"type": "string"},
                        "degree": {"type": "string"},
                        "field": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                        "gpa": {"type": "string"},
                        "notes": {"type": "string"}
                    }
                }
            },
            "projects": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["name", "description", "tech_stack", "impact", "link"],
                    "properties": {
                        "name": {"type": "string"},
                        "description": {"type": "string"},
                        "tech_stack": {"type": "array", "items": {"type": "string"}},
                        "impact": {"type": "string"},
                        "link": {"type": "string"}
                    }
                }
            },
            "certifications": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["name", "issuer", "date", "expires"],
                    "properties": {
                        "name": {"type": "string"},
                        "issuer": {"type": "string"},
                        "date": {"type": "string"},
                        "expires": {"type": "string"}
                    }
                }
            },
            "scoring": {
                "type": "object",
                "additionalProperties": False,
                "required": ["overall_score", "dimension_scores", "missing_keywords", "strengths", "gaps", "recommendations"],
                "properties": {
                    "overall_score": {"type": "integer"},
                    "dimension_scores": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": ["relevance_to_role", "skills_match", "experience_strength", "education_fit", "clarity_and_structure"],
                        "properties": {
                            "relevance_to_role": {"type": "integer"},
                            "skills_match": {"type": "integer"},
                            "experience_strength": {"type": "integer"},
                            "education_fit": {"type": "integer"},
                            "clarity_and_structure": {"type": "integer"}
                        }
                    },
                    "missing_keywords": {"type": "array", "items": {"type": "string"}},
                    "strengths": {"type": "array", "items": {"type": "string"}},
                    "gaps": {"type": "array", "items": {"type": "string"}},
                    "recommendations": {"type": "array", "items": {"type": "string"}}
                }
            },
            "meta": {
                "type": "object",
                "additionalProperties": False,
                "required": ["requirements_version", "model", "analysis_timestamp_utc"],
                "properties": {
                    "requirements_version": {"type": "string"},
                    "model": {"type": "string"},
                    "analysis_timestamp_utc": {"type": "string"}
                }
            }
        }
    },
    "strict": True
}
