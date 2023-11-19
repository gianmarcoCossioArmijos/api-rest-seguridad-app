from app.modelos import ModeloBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import VARCHAR, Integer, DATE, Boolean


class ModeloVehiculo(ModeloBase):
    __tablename__ = "vehiculos"

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    tipo: Mapped[str] = mapped_column(VARCHAR(50))
    placa: Mapped[str] = mapped_column(VARCHAR(10))
    marca: Mapped[str] = mapped_column(VARCHAR(50))
    modelo: Mapped[str] = mapped_column(VARCHAR(100))
    año: Mapped[str] = mapped_column(DATE)
    estado: Mapped[bool] = mapped_column(Boolean, default=True)