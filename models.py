import db
from sqlalchemy import Column, Integer, String, Boolean, DateTime

class Tarea(db.Base):
    __tablename__='tarea'
    id = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False)
    hecha = Column(Boolean)
    categoria = Column(String(200), nullable=False)
    fecha = Column(DateTime)

    def __init__(self,contenido, hecha, categoria, fecha):
        self.contenido = contenido
        self.hecha = hecha
        self.categoria = categoria
        self.fecha = fecha
    
    def __repr__(self):
        return f"Tarea {self.id}: {self.contenido} ({self.hecha})"
    
    def __str__(self):
        return f"Tarea {self.id}: {self.contenido} ({self.hecha})"