from app.modelos import ModeloBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import VARCHAR, Integer, Boolean, DATE, ForeignKey
from bcrypt import hashpw, gensalt, checkpw


class ModeloUsuario(ModeloBase):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    nombres: Mapped[str] = mapped_column(VARCHAR(150))
    nacimiento: Mapped[str] = mapped_column(DATE)
    email: Mapped[str] = mapped_column(VARCHAR(100), unique=True)
    telefono: Mapped[str] = mapped_column(VARCHAR(9))
    clave: Mapped[str] = mapped_column(VARCHAR(255))
    direccion: Mapped[str] = mapped_column(VARCHAR(50))
    estado: Mapped[bool] = mapped_column(Boolean, default=True)
    rol_id: Mapped[int] = mapped_column(Integer, ForeignKey("roles.id"))

    def hash_clave(self):
        encriptar_clave = self.clave.encode("utf-8")
        hash_clave = hashpw(encriptar_clave, gensalt(rounds=10))
        self.clave = hash_clave.decode("utf-8")

    def check_clave(self, clave):
        return checkpw(
            clave.encode("utf-8"),
            self.clave.encode("utf-8")
        )