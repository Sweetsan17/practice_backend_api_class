from flask import request, jsonify
from app.models.student import Student
from app import db


def create_student():
    data = request.get_json()
    students = Student(
        id=data["id"], name=data["name"], age=data["age"], is_active=(data["is_active"])
    )
    db.session.add(students)
    db.session.commit()
    return jsonify({"message": f"Id={id} Student is Created"}), 201


# def get_students():
#     students=Student.query.all()
#     result=[
#         {
#             "id":s.id,
#             "name":s.name,
#             ""
#         }
#     ]
