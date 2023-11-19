from app.modelos import ModeloBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import VARCHAR, Integer, DATE, Boolean, ForeignKey, func


class ModeloUnidad(ModeloBase):
    __tablename__ = "unidades"

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    codigo: Mapped[str] = mapped_column(VARCHAR(50))
    fecha: Mapped[str] = mapped_column(DATE, default=func.current_date())
    tipo_unidad: Mapped[str] = mapped_column(VARCHAR(50))
    chofer: Mapped[str] = mapped_column(VARCHAR(120), nullable=True)
    policia: Mapped[str] = mapped_column(VARCHAR(120), nullable=True)
    operador: Mapped[str] = mapped_column(VARCHAR(120), nullable=True)
    agentes: Mapped[str] = mapped_column(VARCHAR(120))
    descripcion: Mapped[str] = mapped_column(VARCHAR(255))
    estado: Mapped[bool] = mapped_column(Boolean, default=True)
    id_zona: Mapped[int] = mapped_column(Integer, ForeignKey("zonas.id"))
    id_vehiculo: Mapped[int] = mapped_column(Integer, ForeignKey("vehiculos.id"), nullable=True)