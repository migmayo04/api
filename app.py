from flask import Flask
app = Flask (__name__)

@app.route("/")
def welcome():
    return "hello world"

@app.route("/home")
def home():
    return " home page"

from controller import *