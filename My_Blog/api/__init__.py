from combojsonapi.spec import ApiSpecPlugin
from flask_combo_jsonapi import Api

from ..api.article import ArticleList, ArticleDetail
from ..api.author import AuthorList, AuthorDetail
from ..api.user import UserList, UserDetail
from ..api.tag import TagList, TagDetail


def create_api_spec_plugin(app):
    api_spec_plugin = ApiSpecPlugin(
        app=app,
        tags={
            "Tag": "Tag API",
            "User": "User API",
            "Author": "Author API",
            "Article": "Article API",
        }
    )
    return api_spec_plugin


def init_api(app):
    api_spec_plugin = create_api_spec_plugin(app)
    api = Api(app, plugins=[api_spec_plugin, ], )
    api.route(TagList, "tag_list", "/api/tags/", tag="Tag")
    api.route(TagDetail, "tag_detail", "/api/tags/<string:id>/", tag="Tag")
    api.route(UserList, "user_list", "/api/users/", tag="User")
    api.route(UserDetail, "user_detail", "/api/users/<string:id>/", tag="User")
    api.route(AuthorList, "author_list", "/api/authors/", tag="Author")
    api.route(AuthorDetail, "author_detail", "/api/authors/<string:id>/", tag="Author")
    api.route(ArticleList, "article_list", "/api/article/", tag="Article")
    api.route(ArticleDetail, "article_detail", "/api/article/<string:id>/", tag="Article")

