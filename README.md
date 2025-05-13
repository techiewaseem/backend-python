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
