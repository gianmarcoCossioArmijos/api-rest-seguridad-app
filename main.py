from app import app, db
from app import rutas
from app.modelos import ModeloBase

ModeloBase.set_session(db.session)