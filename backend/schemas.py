from pydantic import BaseModel

class StudentInput(BaseModel):
    student_id: str
    student_name: str
    age: float
    study_hours: float
    assignment_completion_rate: float
    attendance_percentage: float
    motivation_level: float
    stress_level: float
    sleep_hours: float