from combojsonapi.event.resource import EventsResource
from flask_combo_jsonapi import ResourceDetail, ResourceList

from ..permissions.article import ArticlePermission
from ..schemas import ArticleSchema
from ..models.database import db
from ..models import Article


class ArticleListEvents(EventsResource):

    def event_get_count(self):
        return {"count": Article.query.count()}


class ArticleList(ResourceList):
    events = ArticleListEvents
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
        "permission_get": [ArticlePermission],
    }
