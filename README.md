
# Teacher Backend API (Flask)

## Endpoints
- `/courses/student/<student_id>` → Returns courses for a student
- `/courses/teacher/<teacher_id>` → Returns courses for a teacher

## Mock Example:
GET http://127.0.0.1:5000/courses/student/student1  
Response:
`json`
`{
  "courses": [
    "Quran Memorization",
    "Islamic Studies"
  ],
  "name": "Omar Al-Hadi",
  "student_id": "student2"
}`

# 🎓 Course Backend API (Python Flask)

This is a simple backend system built using Python and Flask. It provides two API endpoints:

- 📘 **List courses per student**
- 🧑‍🏫 **List courses per teacher**

---

## 📌 Features

- Two REST API endpoints
- Lightweight and fast (uses Flask)
- Mock data for demonstration
- Easily extendable for real databases

---

## 🚀 Installation

To run this project locally, follow the steps below.

### 1. Clone the repository

`
git clone https://github.com/techiewaseem/backend-python.git`

### 2. Navigate into the project directory
`cd backend-python`

### 3. Install Flask globally (if not already installed)
`pip install flask`
⚠️ Make sure you're using pip for Python 3. If needed, use pip3.

### 4. Create your app.py file (if it doesn't exist)
```python
from flask import Flask, jsonify

app = Flask(__name__)

# Mock data
from flask import Flask, jsonify

app = Flask(__name__)

students = {
    "student1": {"name": "Aisha Al-Farsi", "courses": ["Arabic Grammar", "Quran Tajweed"]},
    "student2": {"name": "Omar Al-Hadi", "courses": ["Quran Memorization", "Islamic Studies"]},
    "student3": {"name": "Fatima Al-Sayed", "courses": ["Arabic Literature", "Quran Interpretation"]},
    "student4": {"name": "Yusuf Al-Khalid", "courses": ["Quran Tajweed", "Arabic Grammar"]},
    "student5": {"name": "Layla Al-Rashid", "courses": ["Quran Memorization", "Quran Interpretation"]}
}

teachers = {
    "teacher1": {"name": "Hamdan Bin Khalid", "courses": ["Arabic Grammar", "Arabic Literature"]},
    "teacher2": {"name": "Mariam Al-Najjar", "courses": ["Quran Tajweed", "Quran Memorization"]},
    "teacher3": {"name": "Khalid Al-Mansoori", "courses": ["Islamic Studies", "Quran Interpretation"]},
    "teacher4": {"name": "Sarah Al-Hassan", "courses": ["Arabic Grammar", "Quran Tajweed"]},
    "teacher5": {"name": "Nasser Al-Fahad", "courses": ["Quran Memorization", "Islamic Studies"]}
}

@app.route('/courses/student/<student_id>', methods=['GET'])
def get_student_courses(student_id):
    student = students.get(student_id)
    if student:
        return jsonify({"student_id": student_id, "name": student["name"], "courses": student["courses"]})
    else:
        return jsonify({"error": "Student not found"}), 404

@app.route('/courses/teacher/<teacher_id>', methods=['GET'])
def get_teacher_courses(teacher_id):
    teacher = teachers.get(teacher_id)
    if teacher:
        return jsonify({"teacher_id": teacher_id, "name": teacher["name"], "courses": teacher["courses"]})
    else:
        return jsonify({"error": "Teacher not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

```
### 5. Run the app
`python app.py`

The server will start, and you can visit:

http://localhost:5000/courses/student/student1

http://localhost:5000/courses/teacher/teacher1

to test the endpoints.

