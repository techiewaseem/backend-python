
# Teacher Backend API (Flask)

## Endpoints
- `/courses/student/<student_id>` → Returns courses for a student
- `/courses/teacher/<teacher_id>` → Returns courses for a teacher

## Mock Example:
GET http://127.0.0.1:5000/courses/student/student1  
Response:
```json
{
  "student": "student1",
  "courses": ["Math", "Science"]
}

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

```bash
git clone https://github.com/techiewaseem/backend-python.git
