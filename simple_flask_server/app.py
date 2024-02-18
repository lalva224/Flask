from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://lalva224:1234@localhost/school"

students = [
        {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
        {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
        {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
        {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
        {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
        {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
        {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
        {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
        {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
        {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
    ]

@app.route('/students/',methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/old_students/',methods=['GET'])
def get_old_students():
    #use list comprehension!
    final_student_list = [student for student in students if student['age']>20]
    return jsonify(final_student_list)

@app.route('/young_students/',methods=['GET'])
def get_young_students():
    #use list comprehension!
    final_student_list = [student for student in students if student['age']<21]
    return jsonify(final_student_list)

@app.route('/advance_students/',methods=['GET'])
def get_advanced_students():
    #use list comprehension!
    final_student_list = [student for student in students if student['grade']=='A']
    return jsonify(final_student_list)

@app.route('/student_names/',methods=['GET'])
def get_student_names():
    #use list comprehension!
    final_student_list = [
        {"First Name": student['first_name'],
         "Last Name": student['last_name']

        } 
        for student in students
    ]
    return jsonify(final_student_list)

@app.route('/student_ages/',methods=['GET'])
def get_student_ages():
    #use list comprehension!
    final_student_list = [
        {"First Name": student['first_name'],
         "Last Name": student['last_name'],
          "Age": student['age'],
        } 
        for student in students
    ]
    return jsonify(final_student_list)

if __name__ == '__main__':
    app.run(debug=True)