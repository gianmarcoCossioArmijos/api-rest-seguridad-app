from app.modelos import ModeloBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import VARCHAR, Integer

class ModeloNoticia(ModeloBase):
    __tablename__ = "noticias"

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    imagen: Mapped[str] = mapped_column(VARCHAR(255))
    titulo: Mapped[str] = mapped_column(VARCHAR(50))
    descripcion: Mapped[str] = mapped_column(VARCHAR(120))
    sector: Mapped[str] = mapped_column(VARCHAR(50))