from app.modelos import ModeloBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import VARCHAR, Boolean, Integer


class ModeloRol(ModeloBase):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    nombre: Mapped[str] = mapped_column(VARCHAR(15))
    estado: Mapped[bool] = mapped_column(Boolean, default=True)