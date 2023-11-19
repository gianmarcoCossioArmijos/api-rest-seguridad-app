# Proyecto Aplicacion de Seguridad Ciudadana

- Aplicacion de seguridad ciudadana que permite a los ciudadanos reportar incidencias como: alteracion del orden publico, robos, violencia domestica, infracciones de transito, entre otras.

- Los ciudadanos podran enviar una alerta de emergencia con solo dar click a un boton  en la aplicacion, la cual llegara a seguridad cuidadana. Esto ayudara a atender emergencias como: accidentes de transito, robos, asalto, entre otros.

- Cuenta con una seccion de noticias en la cual se publicaran noticias de interes publico como: calles cerradas por mantenimiento, zonas con altos indices de delincuencia, entre otras.

- Le permitira al area de seguridad cuidadana de una ciudad administrar usuarios, vehiculos de patrullaje, zonas de una ciudad, denuncias, alertas de emergencia, unidades de patrullaje. Lo cual ayudara a un trabajo mas eficiente.

## Requerimientos:

- [x] Conexion a una BD (PostgreSQL o MongoDB)
- [ ] Almenos un CRUD completo (Excluir Usuarios, Roles)
- [x] Controlador con logica(validar que el registro no este eliminado, entre otros)
- [x] Rutas protegidas (JWT)
- [x] Modelos relacionados
- [x] Despliegue en Render (subido y funcional)
- [x] Backend con Flask, Django o NodeJS(Express)
- [x] Documentacion por Swagger o Postman
- [x] Repositorio en Github correctamente documentado con el archivo README.md

## Modelos:

- Usuarios

  | campo     | tipo         | constraint                |
  | --------- | ------------ | ------------------------- |
  | id        | SERIAL       | PRIMARY KEY AUTOINCREMENT |
  | nombres   | VARCHAR(150) | NOT NULL                  |
  | nacimiento| DATE         | NOT NULL                  |
  | email     | VARCHAR(100) | NOT NULL                  |
  | telefono  | VARCHAR(9)   | NOT NULL                  |
  | clave     | VARCHAR(255) | UNIQUE                    |
  | direccion | VARCHAR(50)  | NOT NULL                  |
  | estado    | BOOLEAN      | -                         |
  | rol_id    | INT          | FOREIGN KEY NOT NULL      |

- Roles

  | campo  | tipo     | constraint                |
  | ------ | -------- | ------------------------- |
  | id     | SERIAL   | PRIMARY KEY AUTOINCREMENT |
  | nombre | CHAR(15) | NOT NULL                  |
  | estado | BOOLEAN  | -                         |

- Zonas

  | campo  | tipo     | constraint                |
  | ------ | -------- | ------------------------- |
  | id     | SERIAL   | PRIMARY KEY AUTOINCREMENT |
  | nombre | CHAR(50) | NOT NULL                  |
  | estado | BOOLEAN  | -                         |

- Vehiculos

  | campo  | tipo      | constraint                |
  | ------ | --------- | ------------------------- |
  | id     | SERIAL    | PRIMARY KEY AUTOINCREMENT |
  | tipo   | CHAR(50)  | NOT NULL                  |
  | placa  | CHAR(10)  | NOT NULL                  |
  | marca  | CHAR(50)  | NOT NULL                  |
  | modelo | CHAR(100) | NOT NULL                  |
  | año    | CHAR(10)  | NOT NULL                  |
  | estado | BOOLEAN   | -                         |

- Alertas

  | campo     | tipo      | constraint                |
  | --------- | --------- | ------------------------- |
  | id        | SERIAL    | PRIMARY KEY AUTOINCREMENT |
  | ubicacion | CHAR(100) | NOT NULL                  |
  | fecha     | CHAR(50)  | -                         |
  | hora      | CHAR(10)  | -                         |
  | estado    | BOOLEAN   | -                         |

- Denuncias

  | campo       | tipo      | constraint                |
  | ---------   | --------- | ------------------------- |
  | id          | SERIAL    | PRIMARY KEY AUTOINCREMENT |
  | tipo        | CHAR(50)  | NOT NULL                  |
  | descripcion | CHAR(255) | NOT NULL                  |
  | telefono    | CHAR(9)   | NOT NULL                  |
  | fecha       | DATE      | -                         |
  | hora        | TIMESTAMP | -                         |
  | estado      | CHAR(50)  | -                         |
  | ubicacion   | CHAR(100) | NOT NULL                  |
  | id_usuario  | INT       | NOT NULL                  |

- Unidades

  | campo       | tipo      | constraint                |
  | ---------   | --------- | ------------------------- |
  | id          | SERIAL    | PRIMARY KEY AUTOINCREMENT |
  | codigo      | CHAR(50)  | NOT NULL                  |
  | fecha       | DATE      | -                         |
  | tipo_unidad | CHAR(50)  | NOT NULL                  |
  | chofer      | CHAR(120) | -                         |
  | policia     | CHAR(120) | -                         |
  | operador    | CHAR(120) | -                         |
  | agentes     | CHAR(120) | NOT NULL                  |
  | descripcion | CHAR(255) | NOT NULL                  |
  | estado      | BOOLEAN   | -                         |
  | id_zona     | INT       | NOT NULL                  |
  | id_vehiculo | INT       | -                         |

## Tecnologias:

- Python
- Flask
- Flask SQLAlchemy
- Flask Migrate
- Flask RESTX
- Flask Mail
- PostgreSQL (psycopg2)
- SQLAlquemy Mixins
- Marshmallow SQLAlchemy
- JWT (flask jwt extended)
- Bcrypt

## PIP

```ssh
pip install Flask Flask-Migrate flask-restx Flask-SQLAlchemy psycopg2-binary python-dotenv sqlalchemy-mixins marshmallow-sqlalchemy bcrypt flask-jwt-extended Flask-Mail
```