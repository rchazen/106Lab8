import flask
from flask import Flask, redirect, url_for, jsonify
from flask import request
from flask import abort, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import json

app = Flask(__name__)
app.secret_key = 'shhh'
with app.app_context():
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    db = SQLAlchemy(app)
    admin = Admin(app)

    class User(db.Model):
        __tablename__ = "user"
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String, unique = True, nullable=False)
        password = db.Column(db.String, unique = False, nullable = False)
        name = db.Column(db.String, unique = False, nullable = False)
        teachORstudent =  db.Column(db.String, unique = False, nullable = False)
    class Student(db.Model):
        __tablename__ = "student"
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String, unique = False, nullable = False)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique = True, nullable = False)
        user = db.relationship('User', backref = db.backref('student', lazy = True))
    class Teacher(db.Model):
        __tablename__ = "teacher"
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String, unique = False, nullable = False)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique = True, nullable = False)
        user = db.relationship('User', backref = db.backref('teacher', lazy = True))

    class Classes(db.Model):
        __tablename__ = "classes"
        id = db.Column(db.Integer, primary_key=True)
        course_name = db.Column(db.String, unique = True, nullable=False)
        course_teacherID = db.Column(db.Integer, db.ForeignKey('teacher.id'), unique = False, nullable=False)
        course_numEnrolled = db.Column(db.Integer, unique = False, nullable=False)
        course_capacity = db.Column(db.String, unique = False, nullable=False)
        course_time = db.Column(db.String, unique = False, nullable=False)
        teacher = db.relationship('Teacher', backref = db.backref('classess', lazy = True))

    class Enrollment(db.Model):
        __tablename__ = "enrollment"
        id = db.Column(db.Integer, primary_key = True)
        class_id = db.Column(db.Integer, unique = False, nullable = False)
        student_id = db.Column(db.Integer, unique = False, nullable = False)
        grade = db.Column(db.String, unique = False, nullable = False)
    db.create_all()
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Student, db.session))
    admin.add_view(ModelView(Teacher, db.session))
    admin.add_view(ModelView(Classes, db.session))




@app.route('/')
def index():
    return render_template('index.html')

# Log In Method
@app.route('/login',methods = ["GET", "POST"])
def logIn():
    if request.method == "POST":
        return do_the_login()
    else:
        print("Show the Login Page")
        return render_template('login.html')


    # if request.method == "POST":
    #     name = request.form["nm"]
    #     gd = request.form["gd"]
    #     new_student = Student(name = uname, password = password) 
    #     db.session.add(new_student)
    #     db.session.commit()
    #     return render_template('login.html')
      
    # return render_template('login.html')

# Sign Up Method
@app.route('/signUp',methods = ["GET", "POST"])
def signUp():
    if request.method == "POST":
        uname = request.form["uname"]
        password = request.form["password"]
        name = request.form["name"]
        tOr = request.form["teachORstudent"]
        result = bool(User.query.filter_by(username=uname).first())
        if result == False:
            new_user = User(username = uname, password = password, name = name, teachORstudent = tOr)
            db.session.add(new_user)
            db.session.commit()
            if tOr == "Student":
                new_student = Student(name = name ,  user = new_user)
                db.session.add(new_student)
                db.session.commit()
            if tOr == "Teacher":
                new_teacher = Teacher(name = name ,  user = new_user)
                db.session.add(new_teacher)
                db.session.commit()
        else:
            print("That user exists")
        return render_template('signup.html')
      
    return render_template('signup.html')

def do_the_login():
    print("Do The Login!")
    pass

if __name__ == '__main__':
    app.run()