from app.modelos import ModeloBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import VARCHAR, Integer, DATE, Time,func


class ModeloAlerta(ModeloBase):
    __tablename__ = "alertas"

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    longitud: Mapped[str] = mapped_column(VARCHAR(20))
    latitud: Mapped[str] = mapped_column(VARCHAR(30))
    fecha: Mapped[str] = mapped_column(DATE, default=func.current_date())
    hora: Mapped[str] = mapped_column(Time, default=func.current_timestamp())
    estado: Mapped[str] = mapped_column(VARCHAR(50), default="pendiente")
