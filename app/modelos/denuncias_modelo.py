from app.modelos import ModeloBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import VARCHAR, Integer, DATE, Time, ForeignKey, func


class ModeloDenuncia(ModeloBase):
    __tablename__ = "denuncias"

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    tipo: Mapped[str] = mapped_column(VARCHAR(50))
    descripcion: Mapped[str] = mapped_column(VARCHAR(255))
    telefono: Mapped[str] = mapped_column(VARCHAR(9))
    fecha: Mapped[str] = mapped_column(DATE, default=func.current_date())
    hora: Mapped[str] = mapped_column(Time, default=func.current_timestamp())
    estado: Mapped[str] = mapped_column(VARCHAR(50), default="pendiente")
    ubicacion: Mapped[str] = mapped_column(VARCHAR(100))
    id_usuario: Mapped[int] = mapped_column(Integer, ForeignKey("usuarios.id"))

    def toJson(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "descripcion": self.descripcion,
            "telefono": self.telefono,
            "ubicacion": self.ubicacion,
            "id_usuario": self.id_usuario,
        }