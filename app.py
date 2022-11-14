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
    # Setup
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instance/db.sqlite3"
    db = SQLAlchemy(app)
    admin = Admin(app)

    # Database
    student_classes = db.Table('student_classes',
        db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key = True),
        db.Column('classes_id', db.Integer, db.ForeignKey('classes.id'), primary_key = True)
    )

    class Enrollment(db.Model):
        __tablename__ = "enrollment"
        id = db.Column(db.Integer, primary_key=True)
        grade = db.Column(db.Integer, unique = False, nullable = False)
        # Foreign Key From student.id
        classes_id = db.Column(db.Integer, db.ForeignKey('student.id'), unique = False)
        # Relationship enrollment-class
        classes = db.relationship('Classes', back_populates='enrollment')
        # Foreign Key From class.id
        student_id = db.Column(db.Integer, db.ForeignKey('classes.id'), unique = False)
        # Relationship enrollment-student
        student = db.relationship('Student', back_populates='enrollment')


    class User(db.Model):
        __tablename__ = "user"
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String, unique = True, nullable=False)
        password = db.Column(db.String, unique = False, nullable = False)
        # Relationship User-Student
        student = db.relationship('Student', back_populates='user', uselist=False)
        # Relationship User-Teacher
        teacher = db.relationship('Teacher', back_populates='user', uselist=False)

    class Student(db.Model):
        __tablename__ = "student"
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String, unique=False, nullable=False)
        # Foreign Key From user.id
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique = True, nullable = False)
        # Relationship User-Student
        user = db.relationship('User', back_populates='student', uselist=False)
        # Relationship Enrollment-Student
        enrollment = db.relationship('Enrollment', back_populates='student')
        # Relationship Classes-Student
        classes = db.relationship('Classes',secondary='student_classes', back_populates='student')

    class Teacher(db.Model):
        __tablename__ = "teacher"
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String, unique=False, nullable=False)
        # Foreign Key From user.id
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique = True, nullable = False)
        # Relationship User-Teacher
        user = db.relationship('User', back_populates='teacher', uselist=False)
        # Relationship Classes-Teacher
        classes = db.relationship('Classes', back_populates='teacher')

    class Classes(db.Model):
        __tablename__ = "classes"
        id = db.Column(db.Integer, primary_key=True)
        course_name = db.Column(db.String, unique = True, nullable=False)
        number_enrolled = db.Column(db.Integer, unique = False, nullable=False)
        capacity = db.Column(db.String, unique = False, nullable=False)
        time = db.Column(db.String, unique = False, nullable=False)
        # Foreign Key From teacher.id
        teacher_ID = db.Column(db.String, db.ForeignKey('teacher.id'), unique = False, nullable=False)
        # Relationship Classes-Teacher
        teacher = db.relationship('Teacher', back_populates='classes')
        # Relationship Enrollment-Student
        enrollment = db.relationship('Enrollment', back_populates='classes')
        # Relationship Class-Student
        student = db.relationship('Student', secondary='student_classes', back_populates='classes')
    db.create_all()

    # Admin
    class UserView(ModelView):
        # form_excluded_columns = ['students', 'teachers']
        form_choices = {
            'teachORstudent': [
                     ('Student', 'Student'),
                     ('Teacher', 'Teacher')
                    
                ]
           }
 
    admin.add_view(UserView(User, db.session))
    admin.add_view(ModelView(Student, db.session))
    admin.add_view(ModelView(Teacher, db.session))
    admin.add_view(ModelView(Classes, db.session))
    admin.add_view(ModelView(Enrollment, db.session))

    def __init__(self):
            super(UserView, self).__init__(User, db.session)


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