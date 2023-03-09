import os

from flask import Flask, render_template
from flask_migrate import Migrate
from .views.users import users_app
from .views.articles import articles_app
from .models.database import db
from .views.auth import login_manager, auth_app
from .security import flask_bcrypt

mainapp = Flask(__name__)

mainapp.register_blueprint(users_app, url_prefix="/users")
mainapp.register_blueprint(articles_app, url_prefix="/articles")
mainapp.register_blueprint(auth_app, url_prefix="/auth")

cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
mainapp.config.from_object(f"My_Blog.configs.{cfg_name}")
db.init_app(mainapp)
login_manager.init_app(mainapp)
migrate = Migrate(mainapp, db)
flask_bcrypt.init_app(mainapp)


@mainapp.route("/")
def index():
    return render_template("index.html")


@mainapp.cli.command("create-admin")
def create_admin():
    from .models import User
    admin = User(username="admin", email='admin@default.com', is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or "adminpass"
    db.session.add(admin)
    db.session.commit()
    print("done! created admin:", admin)


@mainapp.cli.command("create-default-users")
def create_users():
    from .models import User
    import string, random
    for i in range(5):
        name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        create_user = User(username=name, email=f'{name}@default.com',
                           avatar=f'/static/img/{random.randrange(1, 4)}.jpg', password='1234567890')
        db.session.add(create_user)
        db.session.commit()
        print("done! created users:", create_user)


@mainapp.cli.command("create-articles")
def create_articles():
    from .models import User
    from .models import Article
    import string, random
    users = User.query.all()
    for user in users:
        text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=70))
        create_article = Article(title=f'Article by {user.username}', author_id=user.id, text=text)
        db.session.add(create_article)
        db.session.commit()
        print("done! created article:", create_article)
