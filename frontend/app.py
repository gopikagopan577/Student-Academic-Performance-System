import streamlit as st
import requests

st.title('Student Academic Performance Prediction')

st.write('Enter the student details below to predict the final grade')


student_id = st.text_input('Student ID')
student_name = st.text_input('Student Name')

age = st.number_input('Age', min_value=15, max_value=23, value=18)

study_hours = st.number_input('Study Hours', min_value=0, max_value=8, value=5)

assignment_completion_rate = st.number_input('Assignment Completion Rate(%)', min_value=39.06, max_value=100.00, value=80.00)

attendance_percentage = st.number_input('Attendance Percentage (%)', min_value=48.94, max_value=100.00, value=80.00)

motivation_level = st.number_input('Motivation Level', min_value=1, max_value=10, value=5)

stress_level = st.number_input('Stress Level', min_value=1, max_value=10, value=5)

sleep_hours = st.number_input('Sleep Hours', min_value=3, max_value=10, value=7)


if st.button('Predict Final Grade'):

    data = {
        'student_id': student_id,
        'student_name': student_name,
        'age': age,
        'study_hours': study_hours,
        'assignment_completion_rate': assignment_completion_rate,
        'attendance_percentage': attendance_percentage,
        'motivation_level': motivation_level,
        'stress_level': stress_level,
        'sleep_hours': sleep_hours
    }

    response = requests.post('http://backend:8000/predict', json=data)

    if response.status_code == 200:

        result = response.json()

        st.success('Prediction completed')

        st.write('Student ID:', result['student_id'])
        st.write('Student Name:', result['student_name'])

        st.write(f"Predicted Final Grade: {result['predicted_final_grade']} / 100")

        if result['result'] == 'PASS':
            st.success('Result: PASS')
        else:
            st.error("Result: FAIL")

    else:
        st.error('Unable to get prediction from the API')