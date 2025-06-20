from db import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Imagen(Base):
    __tablename__ = "imagenes"
    id= Column(Integer, primary_key=True)
    fecha_creacion = Column(Date)
    url = Column(String(200))
    tipo_archivo = Column(String(10))
    
    noticia_id = Column(Integer, ForeignKey("noticias.id"))  # clave foránea
    noticia = relationship("Noticia", back_populates="imagenes")