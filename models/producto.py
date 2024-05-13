from pydantic import BaseModel, Field
from typing import Optional

class Producto(BaseModel):
    id: Optional[int] = None 
    name: str = Field(default="Nuevo producto", min_length=5, max_length=15)
    precio: float = Field(default=0, ge=0, le=1000)
    disponible: int = Field(default=0, gt=0)