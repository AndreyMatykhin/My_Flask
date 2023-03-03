from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from ..models import User

users_app = Blueprint("users_app", __name__)

USERS_LIST = {
    1: {'name': 'Tom', 'avatar': '/static/img/1.jpg'},
    2: {'name': 'Jack', 'avatar': '/static/img/2.jpg'},
    3: {'name': 'Becky', 'avatar': '/static/img/3.jpg'}
}


@users_app.route("/", endpoint='list')
def users_list():
    users = User.query.all()
    return render_template("users/list.html", users=users)


@users_app.route("/<string:user_id>/", endpoint='details')
def user_details(user_id: str):
    user = User.query.filter_by(id=user_id).one_or_none()
    if user is None:
        raise NotFound(f"User #{user_id} doesn't exist!")
    return render_template("users/details.html", user=user)
