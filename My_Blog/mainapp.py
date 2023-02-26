from flask import Flask, request

mainapp = Flask(__name__)


@mainapp.route("/")
def index():
    if request.args != {}:
        name = request.args.get("name")
        surname = request.args.get("surname")
        return f"Hello, {name}{' ' + surname or ''}! This is my first project on Flask!"
    else:
        return f"Hello, Unknown User! This is my first project on Flask!"