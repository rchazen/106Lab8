import flask
from flask import Flask, redirect, url_for, jsonify
from flask import request
from flask import abort, render_template
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)




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