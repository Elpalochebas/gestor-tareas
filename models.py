import db
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

class Tarea(db.Base):
    __tablename__='tarea'
    id = Column(Integer, primary_key=True, autoincrement=True)
    contenido = Column(String(200), nullable=False)
    hecha = Column(Boolean)
    categoria = Column(String(200), nullable=False)
    fecha_creacion = Column(DateTime)
    fecha_entrega = Column(DateTime)
    fecha_creacion_str:str
    fecha_entrega_str:str

    def __init__(self,contenido, hecha, categoria, fecha_creacion, fecha_entrega):
        self.contenido = contenido
        self.hecha = hecha
        self.categoria = categoria 
        self.fecha_creacion = fecha_creacion
        self.fecha_entrega = fecha_entrega
    
    def date_format (self):
        self.fecha_creacion_str = datetime.strftime(self.fecha_creacion, '%Y-%m-%d %H:%M')
        self.fecha_entrega_str = datetime.strftime(self.fecha_entrega, '%Y-%m-%d %H:%M')
       
    
    def __repr__(self):
        return f"Tarea {self.id}: {self.contenido} ({self.hecha})"
    
    def __str__(self):
        return f"Tarea {self.id}: {self.contenido} ({self.hecha})"