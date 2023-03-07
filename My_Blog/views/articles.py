from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from werkzeug.exceptions import NotFound
from ..models import Article

articles_app = Blueprint("articles_app", __name__)


@articles_app.route("/", endpoint='list')
def list():
    return render_template("articles/list.html", articles=Article.query.all())


@articles_app.route("/author/<string:author_id>/", endpoint='articles_by_author')
def articles_by_author(author_id: str):
    return render_template("articles/articles_by_author.html", articles=Article.query.filter_by(author_id=author_id))


@articles_app.route("/<string:article_id>/", endpoint='details')
def details(article_id: int):
    if current_user.is_authenticated:
        article = Article.query.filter_by(id=article_id).one_or_none()
        if article is None:
            raise NotFound(f"User #{article_id} doesn't exist!")
        return render_template('articles/details.html', article=article)
    return redirect(url_for("auth_app.login"))
