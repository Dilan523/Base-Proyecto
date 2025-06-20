from db import Base
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer,
                        primary_key=True)
    nombre_usuario = Column(String(60))
    apellido_usuario = Column(String(60))
    correo_usuario = Column(String(60))
    contrasena_usuario = Column(String(60))
    estado_editor = Column(Boolean)
    estado_escritor = Column(Boolean)

    #comentarios = relationship("Comentario", back_populates="usuario")
    #clave foranea
    rol_id = Column(Integer, 
                    ForeignKey("roles.id"))
    # Relación con SQLAlchemy para acceso sencillo
    #rol = relationship("Rol", back_populates="usuarios")