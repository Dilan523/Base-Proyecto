from db import Base
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Comentario():
    __tablename__ = "comentarios"
    id = Column(Integer, primary_key=True)
    fecha_creacion = Column(Date)
    contenido = Column(String(200))

    # # # Clave foránea
    oticia_id = Column(Integer,ForeignKey("noticias.id"))
    # # # clave foránea
    usuario_id = Column(Integer,ForeignKey("usuarios.id"))
    
