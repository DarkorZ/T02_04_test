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

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    precio: Optional[float] = None
    stock: Optional[int] = None
    categoria: Optional[str] = None
    active: Optional[bool] = None

class Cliente(BaseModel):
    id: str # Cédula o RUC [cite: 500]
    nombre: str
    email: str
    puntosFidelidad: int = 0


class DetalleVenta(BaseModel):
    producto_id: str
    nombre_producto: str
    cantidad: int
    precio_unitario: float
    subtotal: float

class Venta(BaseModel):
    id_factura: str
    fecha: datetime = Field(default_factory=datetime.now)
    cliente_id: str
    items: List[DetalleVenta]
    total: float

# --- MODELO PARA LOS ITEMS QUE VIENEN EN EL CARRITO ---
class ItemCarrito(BaseModel):
    id: str        # El ID del producto (ej: "P01")
    cantidad: int  # Cuántas unidades compra    