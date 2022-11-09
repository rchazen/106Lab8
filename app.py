import flask
from flask import Flask, redirect, url_for, jsonify
from flask import request
from flask import abort, render_template
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
with app.app_context():
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    db = SQLAlchemy(app)

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String, unique = True, nullable=False)
        password = db.Column(db.String, unique = False, nullable = False)
    db.create_all()



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
        new_user = User(username = uname, password = password) 
        db.session.add(new_user)
        db.session.commit()
        return render_template('signup.html')
      
    return render_template('signup.html')

def do_the_login():
    print("Do The Login!")
    pass

if __name__ == '__main__':
    app.run()