import json
import os
from .models import Interview
from typing import List

class InterviewMemory:
    def __init__(self, storage_path="interview_history.json"):
        self.storage_path = storage_path
        if not os.path.exists(self.storage_path):
            with open(self.storage_path, "w") as f:
                json.dump([], f)

    def save_interview(self, interview: Interview):
        interviews = self.list_interviews()
        interviews.append(interview.dict())
        with open(self.storage_path, "w") as f:
            json.dump(interviews, f, default=str)

    def list_interviews(self) -> List[dict]:
        with open(self.storage_path, "r") as f:
            return json.load(f)

    def get_interview_by_id(self, interview_id: str) -> dict:
        interviews = self.list_interviews()
        for interview in interviews:
            if interview["id"] == interview_id:
                return interview
        return None
