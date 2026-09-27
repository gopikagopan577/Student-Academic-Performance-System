from fastapi import FastAPI
import joblib
import  pandas  as pd

from backend.schemas import StudentInput

app = FastAPI(title= 'Student Prediction System API')

## to load model
model = joblib.load('models/model.pkl')

@app.get('/')
def home():
    return {'message': 'API is running'}


@app.post('/predict')
def predict(student: StudentInput):

    data = pd.DataFrame([{
        'age': student.age,
        'study_hours': student.study_hours,
        'assignment_completion_rate': student.assignment_completion_rate,
        'attendance_percentage': student.attendance_percentage,
        'motivation_level': student.motivation_level,
        'stress_level': student.stress_level,
        'sleep_hours': student.sleep_hours
    }])

    prediction = model.predict(data)[0]

    if prediction >= 40:
        result = 'PASS'

    else:
        result = 'FAIL'    

    return {
        'student_id': student.student_id,
        'student_name': student.student_name,
        'predicted_final_grade': round(float(prediction), 2),
        'result': result
    }