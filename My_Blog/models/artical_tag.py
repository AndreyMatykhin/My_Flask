from sqlalchemy import Table, Column, String, ForeignKey
from .database import db

article_tag_association_table = Table(
    "article_tag_association",
    db.metadata,
    Column("article_id", String(length=36), ForeignKey("article.id"), nullable=False),
    Column("tag_id", String(length=36), ForeignKey("tag.id"), nullable=False),
)
