from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from werkzeug.exceptions import NotFound
from .users import USERS_LIST

articles_app = Blueprint("articles_app", __name__)

ARTICLES_LIST = {
    1: {'title': 'Cheburashka', 'author': 1,
        'text': '18 процентов россиян захотели отправиться в туры по городам в 2023 году.'
                ' Большинство россиян планирует отправиться в прогулки по городам, активные '
                'туры или проведет отпуск на море. Об этом стало известно из опроса сервиса '
                'путешествий «Туту», результаты которого поступили в редакцию «Ленты.ру».'},
    2: {'title': 'Bloomberg', 'author': 2,
        'text': 'Так, 18 процентов участников опроса отметили, что их привлекает архитектура '
                'красивых городов. Чуть меньше, 16 процентов респондентов, раскрыли, что хотят '
                'отправиться в активные туры по России: сплавы, треккинг или велопоходы. '},
    3: {'title': 'Online47.ru', 'author': 3,
        'text': 'Такое же количество туристов предпочло классический отпуск на море на отечественных курортах.'
                'Примерно каждый десятый респондент (11 процентов голосов) планирует отдохнуть в 2023 году на '
                'зарубежных пляжных направлениях, например отправиться на Мальдивы, в Таиланд или в Объединенные '
                'Арабские Эмираты. Еще восемь процентов признались, что хотели бы попробовать в этом году пожить '
                'на природе — в глэмпинге или палатке.'},
    4: {'title': 'Online47.ru', 'author': 3,
        'text': 'Такое же количество туристов предпочло классический отпуск на море на отечественных курортах.'
                ' Примерно каждый десятый респондент (11 процентов голосов) планирует отдохнуть в 2023 году на '
                'зарубежных пляжных направлениях, например отправиться на Мальдивы, в Таиланд или в Объединенные '
                'Арабские Эмираты. '},
    5: {'title': 'ТАСС', 'author': 2,
        'text': ' По семь процентов туристов планируют поехать '
                'в страны Европы, отправиться в гастротур или в образовательную поездку с музеями, '
                'выставками и экскурсиями. Путешествие в страны ближнего зарубежья (Армения, Грузия и Узбекистан)'
                ' запланировали шесть процентов респондентов, еще четыре процента выбрали круиз. '},
    6: {'title': 'Reddit', 'author': 1,
        'text': 'Ранее в феврале стало известно, что самыми востребованными городами у'
                ' россиян для отдыха на 8 марта стали Сочи, Москва и Санкт-Петербург.'}
}


@articles_app.route("/", endpoint='list')
def list():
    return render_template("articles/list.html", articles=ARTICLES_LIST, author=USERS_LIST)


@articles_app.route("/author/<string:author_id>/", endpoint='articles_by_author')
def articles_by_author(author_id: str):
    author_name = USERS_LIST[1]['name']
    articles = {el: ARTICLES_LIST[el] for el in ARTICLES_LIST if ARTICLES_LIST[el]['author'] == 1}
    return render_template("articles/articles_by_author.html", articles=articles, author_name=author_name)


@articles_app.route("/<int:article_id>/", endpoint='details')
def details(article_id: int):
    if current_user.is_authenticated:
        try:
            article = ARTICLES_LIST[article_id]
            author_name = USERS_LIST[ARTICLES_LIST[article_id]['author']]['name']
        except KeyError:
            raise NotFound(f"User #{article_id} doesn't exist!")
        return render_template('articles/details.html', article_id=article_id, article=article, author_name=author_name)
    return redirect(url_for("auth_app.login"))
