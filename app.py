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

    class Users(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String, unique = True, nullable=False)
        password = db.Column(db.Float, unique = False, nullable = False)
    db.create_all()




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def logIn():
    return render_template('login.html')

@app.route('/signup')
def signUp():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run()