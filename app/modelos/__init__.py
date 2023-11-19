from app import db
from sqlalchemy_mixins import AllFeaturesMixin


class ModeloBase(db.Model, AllFeaturesMixin):
    __abstract__ = True
    