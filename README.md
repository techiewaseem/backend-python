
# Teacher Backend API (Flask)

## Endpoints
- `/courses/student/<student_id>` → Returns courses for a student
- `/courses/teacher/<teacher_id>` → Returns courses for a teacher

## Mock Example:
GET http://127.0.0.1:5000/courses/student/student1  
Response:
`json`
`{
  "student": "student1",
  "courses": ["Math", "Science"]
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
```
from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
students = {
    "student1": ["Math", "Science"],
    "student2": ["English", "History"]
}

teachers = {
    "teacher1": ["Math", "Physics"],
    "teacher2": ["English", "Literature"]
}

@app.route('/courses/student/<student_id>')
def get_student_courses(student_id):
    return jsonify({student_id: students.get(student_id, [])})

@app.route('/courses/teacher/<teacher_id>')
def get_teacher_courses(teacher_id):
    return jsonify({teacher_id: teachers.get(teacher_id, [])})

if __name__ == '__main__':
    app.run(debug=True)
```
### 5. Run the app
`python app.py`

The server will start, and you can visit:

http://localhost:5000/courses/student/student1

http://localhost:5000/courses/teacher/teacher1

to test the endpoints.

