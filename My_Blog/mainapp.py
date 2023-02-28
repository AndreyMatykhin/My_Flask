from flask import Flask, render_template
from .views.users import users_app
from .views.articles import articles_app

mainapp = Flask(__name__)

mainapp.register_blueprint(users_app, url_prefix="/users")
mainapp.register_blueprint(articles_app, url_prefix="/articles")

@mainapp.route("/")
def index():
    return render_template("index.html")
