from flask import Blueprint, render_template, redirect, url_for, request, current_app
from flask_login import current_user, login_required
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from ..forms.article import CreateArticleForm
from ..models import Article, Author, Tag
from ..models.database import db

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
        article = Article.query.filter_by(id=article_id).options(
            joinedload(Article.tags)).one_or_none()
        if article is None:
            raise NotFound(f"User #{article_id} doesn't exist!")
        return render_template('articles/details.html', article=article)
    return redirect(url_for("auth_app.login"))


@articles_app.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]
    if request.method == "POST" and form.validate_on_submit():
        article = Article(title=form.title.data.strip(), text=form.text.data)
        db.session.add(article)
        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                article.tags.append(tag)
        if current_user.author:
            article.author = current_user.author
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author = author

        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
            error = "Could not create article!"
        else:
            return redirect(url_for("articles_app.details", article_id=article.id))

    return render_template("articles/create.html", form=form, error=error)
