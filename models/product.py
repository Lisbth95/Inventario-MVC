class Product:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def toDBCollection(self):
        return{
            'nombre': self.nombre,
            'precio': self.precio,
            'cantidad': self.cantidad
        }