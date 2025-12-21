#Creacion del esquema del modelo
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class EntityBase(BaseModel):
    id: str
    fecha_Creacion: datetime = Field(default_factory=datetime.now)
    autor: str = "Equipo de Desarrollo"

class Producto(EntityBase):
    nombre: str
    codigoBarras: str
    precio: float
    categoria: str
    stock: int
    active: bool = True





