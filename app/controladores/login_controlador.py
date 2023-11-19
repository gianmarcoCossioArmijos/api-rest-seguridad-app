from app import db, mail
from app.modelos.usuarios_modelo import ModeloUsuario
from http import HTTPStatus
from flask_jwt_extended import create_access_token, create_refresh_token
from secrets import token_hex
from flask_mail import Message


class LoginControlador:

    def __init__(self):
        self.db = db
        self.model = ModeloUsuario

    def iniciar_sesion(self, datos):
        try:
            email = datos["email"]
            clave = datos["clave"]
            if not email:
                return {
                    "mensaje": "Debe ingresar un email"
                }, HTTPStatus.BAD_REQUEST
            if not clave:
                return {
                    "mensaje": "Debe ingresar contraseña"
                }, HTTPStatus.BAD_REQUEST
            registro = self.model.where(estado=True, email=email).first()
            if registro:
                if registro.check_clave(clave):
                    id_usuario = registro.id
                    access_token = create_access_token(identity=id_usuario)
                    refresh_token = create_refresh_token(identity=id_usuario)
                    return {
                        "access_token": access_token,
                        "refresh_token": refresh_token
                    }, HTTPStatus.OK
            return {
                "mensaje": f"No se encontro al usuario {email}"
            }, HTTPStatus.NOT_FOUND

        except Exception as e:
            return {
                "message": "Ocurrio un error al iniciar sesion",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        finally:
            db.session.close()

    def refresh_token(self, identity):
        try:
            access_token = create_access_token(identity=identity)
            return {
                "access_token": access_token
            }, HTTPStatus.OK

        except Exception as e:
            return {
                "message": "Ocurrio un error al crear nuevo access token",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def reseteo_clave(self, datos):
        try: 
            email = datos["email"]
            registro = self.model.where(estado=True, email=email).first()
            if registro:
                nueva_clave = token_hex(5)
                registro.clave = nueva_clave
                registro.hash_clave()
                self.db.session.add(registro)
                self.db.session.commit()
                mensaje = Message(
                    subject='Alerta Jaen - Recuperar cuenta',
                    sender=('Alerta Jaen'),
                    recipients=[email],
                    body=f'Tu contraseña se ha restablecido, copia el siguiente codigo para recuperar tu cuenta y cambiar tu contraseña: {nueva_clave}'
                )
                mail.send(mensaje)
                return {
                    "mensaje": "La contraseña ha sido restablecida"
                }, HTTPStatus.OK
            return {
                "mensaje": f"No se encontro al usuario con id {id}"
            }, HTTPStatus.NOT_FOUND

        except Exception as e:
            self.db.session.rollback()
            return {
                "message": "Ocurrio un error al resetear contraseña",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        finally:
            self.db.session.close()