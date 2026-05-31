from flask import request, jsonify
from app.models.student import Student
from app import db


def create_student():
    data = request.get_json()
    student = Student(name=data["name"], age=data["age"])
    db.session.add(student)
    db.session.commit()
    return jsonify({"message": " Student is Created"}), 201
