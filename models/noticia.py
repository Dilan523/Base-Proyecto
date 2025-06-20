from db import Base
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Noticia(Base):
    __tablename__ = "noticias"
    id = Column(Integer,
                primary_key=True)
    fecha_creacion = Column(Date)
    estado = Column(Boolean)
    titulo = Column(String(60))
    introduccion = Column(String(200))
    contenido = Column(String(2000))
    imagen = Column(String(200))
    estado = Column(Integer)

    
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    comentario_id = Column(Integer, ForeignKey("comentarios.id"))
    usuario_revisor_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario_escritor_id = Column(Integer, ForeignKey("usuarios.id"))

    
    imagenes = relationship("Imagen", back_populates="noticia") #plural y coincide
    comentarios = relationship("Comentario", back_populates="noticia")
    categoria = relationship("Categoria", back_populates="noticias")