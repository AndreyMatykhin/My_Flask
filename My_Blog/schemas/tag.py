from combojsonapi.utils import Relationship
from marshmallow_jsonapi import Schema, fields


class TagSchema(Schema):
    class Meta:
        type_ = "tag"
        self_url = "tag_detail"
        self_url_kwargs = {"id": "<id>"}
        self_url_many = "tag_list"

    id = fields.String()
    name = fields.String(allow_none=False, required=True)
    articles = Relationship(
        nested="ArticleSchema",
        attribute="articles",
        related_view="article_detail",
        related_view_kwargs={"id": "<id>"},
        schema="ArticleSchema",
        type_="article",
        many=True,
    )
