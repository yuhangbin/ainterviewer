from fastapi import FastAPI, HTTPException
from .models import Interview
from .memory import InterviewMemory
from typing import List

app = FastAPI()
memory = InterviewMemory()

@app.post("/interviews/", response_model=Interview)
def create_interview(interview: Interview):
    memory.save_interview(interview)
    return interview

@app.get("/interviews/", response_model=List[Interview])
def get_all_interviews():
    return memory.list_interviews()

@app.get("/interviews/{interview_id}", response_model=Interview)
def get_interview(interview_id: str):
    interview = memory.get_interview_by_id(interview_id)
    if not interview:
        raise HTTPException(status_code=404, detail="Interview not found")
    return interview
