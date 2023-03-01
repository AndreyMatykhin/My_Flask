from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

users_app = Blueprint("users_app", __name__)

USERS_LIST = {
    1: {'name': 'Tom', 'avatar': '/static/img/1.jpg'},
    2: {'name': 'Jack', 'avatar': '/static/img/2.jpg'},
    3: {'name': 'Becky', 'avatar': '/static/img/3.jpg'}
}


@users_app.route("/", endpoint='list')
def users_list():
    return render_template("users/list.html", users=USERS_LIST)


@users_app.route("/<int:user_id>/", endpoint='details')
def user_details(user_id: int):
    try:
        user_name = USERS_LIST[user_id]['name']
    except KeyError:
        raise NotFound(f"User #{user_id} doesn't exist!")
    return render_template('users/details.html', user_id=user_id, user_name=user_name)
