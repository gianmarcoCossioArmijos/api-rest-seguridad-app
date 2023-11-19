from app.modelos import ModeloBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import VARCHAR, Integer, Boolean


class ModeloZona(ModeloBase):
    __tablename__ = "zonas"

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    nombre: Mapped[str] = mapped_column(VARCHAR(50))
    estado: Mapped[bool] = mapped_column(Boolean, default=True)