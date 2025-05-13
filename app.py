from flask import Flask, jsonify

app = Flask(__name__)

# Mock data
students = {
    "student1": ["Math", "Science"],
    "student2": ["History", "English"]
}

teachers = {
    "teacher1": ["Math", "Physics"],
    "teacher2": ["English", "Literature"]
}

@app.route('/courses/student/<student_id>', methods=['GET'])
def get_student_courses(student_id):
    return jsonify({"student": student_id, "courses": students.get(student_id, [])})

@app.route('/courses/teacher/<teacher_id>', methods=['GET'])
def get_teacher_courses(teacher_id):
    return jsonify({"teacher": teacher_id, "courses": teachers.get(teacher_id, [])})

if __name__ == '__main__':
    app.run(debug=True)
