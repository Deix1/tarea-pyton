#Clase CarroCompras que: (1) tenga método agregar_articulo(nombre, precio) 
#que guarde en un diccionario {nombre: precio}; (2) tenga método total_carrito() que retorne la suma de todos 
#los precios; (3) tenga método articulos_por_rango(precio_min, precio_max) que retorne una lista con artículos 
#dentro del rango.
class CarroCompras:

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, precio):
        self.productos[nombre] = precio

    def total(self):
        suma = 0

        for precio in self.productos.values():
            suma = suma + precio

        return suma

    def productos_por_precio(self, minimo, maximo):
        resultado = []

        for nombre, precio in self.productos.items():
            if precio >= minimo and precio <= maximo:
                resultado.append(nombre)

        return resultado


carro = CarroCompras()

carro.agregar_producto("Pan", 1.50)
carro.agregar_producto("Leche", 2.00)
carro.agregar_producto("Arroz", 3.50)
carro.agregar_producto("Pollo", 8.00)

print("Productos:", carro.productos)
print("Total:", carro.total())
print("Productos entre $2 y $5:", carro.productos_por_precio(2, 5))