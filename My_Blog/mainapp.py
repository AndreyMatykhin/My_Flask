from flask import Flask, render_template
from .views.users import users_app
from .views.articles import articles_app
from .models.database import db
from .views.auth import login_manager, auth_app

mainapp = Flask(__name__)

mainapp.register_blueprint(users_app, url_prefix="/users")
mainapp.register_blueprint(articles_app, url_prefix="/articles")
mainapp.register_blueprint(auth_app, url_prefix="/auth")

mainapp.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/blog.db"
mainapp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
mainapp.config["SECRET_KEY"] = "abcdefg123456"
db.init_app(mainapp)
login_manager.init_app(mainapp)


@mainapp.route("/")
def index():
    return render_template("index.html")


@mainapp.cli.command("init-db")
def init_db():
    db.create_all()
    print("done!")


@mainapp.cli.command("create-superusers")
def create_superusers():
    from .models import User
    admin = User(username="admin", email='admin@default.com', is_staff=True)
    db.session.add(admin)
    db.session.commit()
    print("done! created superusers:", admin)


@mainapp.cli.command("create-default-users")
def create_users():
    from .models import User
    import string, random
    for i in range(5):
        name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        create_user = User(username=name, email=f'{name}@default.com',
                           avatar=f'/static/img/{random.randrange(1, 4)}.jpg')
        db.session.add(create_user)
        db.session.commit()
        print("done! created users:", create_user)
