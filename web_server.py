from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
#__name__ is the location of our file
app = Flask(__name__)
#database configuration for flask
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://lalva224:1234@localhost/school"
#create database object
db = SQLAlchemy(app)

#create Table specification
#indicates student is a table
class students(db.Model):
    #arguments for db.Column: 
    #db.Column(type, primary_key=False, unique=False, nullable=True, index=False, default=None, server_default=None, ...)
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    birthdate = db.Column(db.DateTime)
    address_id = db.Column(db.Integer)
"""
school=# \d students
                                      Table "public.students"
   Column   |          Type          | Collation | Nullable |               Default
------------+------------------------+-----------+----------+--------------------------------------
 id         | integer                |           | not null | nextval('students_id_seq'::regclass)
 first_name | character varying(255) |           | not null |
 last_name  | character varying(255) |           | not null |
 birthdate  | date                   |           | not null |
 address_id | integer                |           | not null | 
"""

#under localhost:5000/sutdents it will perform a get request. It creates a json from the array of dicts, students.
@app.route('/students',methods=['GET'])
def get_student():
    #retrieve all rows for student table
    student_row = students.query.all()
    #create array of dicts
    student_list = [
        {'id':student.id, 'f_name': student.first_name,'l_name':student.last_name,'date':student.birthdate,'address_id':student.address_id}
        for student in student_row
    ]
    #jsonify the list of dicts
    return jsonify(student_list)

#This will only run if this is the main file being run and not an import.
if __name__ == '__main__':
    #debug allows any changes in code to be reflected in web page without a reload
    app.run(debug=True)