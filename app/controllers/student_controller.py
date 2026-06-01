from flask import request, jsonify
from app.models.student import Student
from app import db


def create_student():
    data = request.get_json()
    # vaildation
    if not data:
        return jsonify({"error": "you must put the value"}), 400
    elif not data.get("name"):
        return jsonify({"error": "Name is required"}), 400
    elif not data.get("age"):
        return jsonify({"error": "Age is required"}), 400

    student = Student(name=data["name"], age=data["age"])
    db.session.add(student)
    db.session.commit()
    return jsonify({"message": " Student is Created"}), 201


def get_students():
    students = Student.query.all()
    results = [
        {"id": s.id, "name": s.name, "age": s.age, "is_active": s.is_active}
        for s in students
    ]
    return jsonify(results)
