from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class QA(BaseModel):
    question: str
    answer: str

class Interview(BaseModel):
    id: str
    interview_type: str  # "mock" or "real"
    timestamp: datetime
    questions_and_answers: List[QA]
    metadata: Optional[Dict[str, str]] = Field(default_factory=dict)
