from fastapi import APIRouter, Path, Query
from models.producto import Producto

router = APIRouter() 

productos = [
    {
        "id": 1,
        "name": "Producto 1",
        "precio": 20,
        "disponible": 89
    },
    
    {
        "id": 2,
        "name": "Producto 2",
        "precio": 25,
        "disponible": 10 
    }
]


@router.get("/productos")
def get_productos_1():
    return productos  


#Esta es la funcion que se utliza para mostrar DATOS
@router.get("/productos{id}")
def get_producto_2(id: int = Path(gt=0)):
    return list(filter(lambda item: item["id"] == id, productos))

#Esta es la funcion que se utliza para mostrar DATOS
@router.get("/productos/") 
def productos_disponible(disponible: int, precio: float = Query(gt=0 )):
    return list(filter(lambda item: item["disponible"] == 
                    disponible and item["precio"] == precio, productos))


#Esta es la funcion que se utliza para enviar DATOS
@router.post('/productos')
def crear_producto(producto: Producto):
    productos.append(producto)
    return productos

#Esta es la funcion que se utliza para actualizar DATOS
@router.put('/productos/{ id}')
def actualizar_datos(id: int, producto: Producto):
    for index, item in enumerate(productos):
        if item['id'] == id:
            productos[index]['name'] = producto.name 
            productos[index]['disponible'] = producto.disponible
            productos[index]['precio'] = producto.precio
    return productos        

#Esta es la funcion que se utliza para eliminar DATOS
@router.delete('/productos/{id}')
def eliminar_productos(id: int):
    for item in productos:
        if item['id'] == id:
            productos.remove(item)
    return productos          
