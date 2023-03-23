from flask_combo_jsonapi import ResourceDetail, ResourceList
from ..schemas import ArticleSchema
from ..models.database import db
from ..models import Article


class ArticleList(ResourceList):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }
