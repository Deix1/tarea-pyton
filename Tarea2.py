#Clase CarroCompras que: (1) tenga método agregar_articulo(nombre, precio) que guarde en un 
#diccionario {nombre: precio}; (2) tenga método total_carrito() que retorne la suma de todos los precios; (3)
#tenga método articulos_por_rango(precio_min, precio_max) que retorne una lista con artículos dentro del 
#rango.
class AnalizadorTexto:

    def __init__(self):
        self.palabras = []
        self.unicas = set()

    def agregar_palabra(self, palabra):
        self.palabras.append(palabra)
        self.unicas.add(palabra)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)

    def cantidad_unicas(self):
        return len(self.unicas)


analizador = AnalizadorTexto()

analizador.agregar_multiples("hola", "casa", "hola", "perro", "casa")

print("Palabras:", analizador.palabras)
print("Palabras unicas:", analizador.unicas)
print("Cantidad de palabras unicas:", analizador.cantidad_unicas())