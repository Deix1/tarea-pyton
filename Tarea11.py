#Clase ContadorFrecuencia que: (1) tenga método agregar_elemento(elemento) que guarde en un 
#diccionario contando repeticiones; (2) tenga método elemento_mas_frecuente() que retorne el elemento 
#con mayor frecuencia; (3) tenga método frecuencia_elemento(elemento) que retorne cuántas veces aparece.
class ContadorFrecuencia:

    def __init__(self):
        self.frecuencias = {}

    def agregar(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] = self.frecuencias[elemento] + 1
        else:
            self.frecuencias[elemento] = 1

    def agregar_multiples(self, *elementos):
        for elemento in elementos:
            self.agregar(elemento)

    def mas_frecuente(self):
        elemento_mayor = ""
        frecuencia_mayor = 0

        for elemento, frecuencia in self.frecuencias.items():
            if frecuencia > frecuencia_mayor:
                frecuencia_mayor = frecuencia
                elemento_mayor = elemento

        return elemento_mayor

    def frecuencia_de(self, elemento):
        if elemento in self.frecuencias:
            return self.frecuencias[elemento]
        else:
            return 0


contador = ContadorFrecuencia()

contador.agregar_multiples(
    "rojo",
    "azul",
    "rojo",
    "verde",
    "azul",
    "rojo"
)

print("Frecuencias:", contador.frecuencias)
print("Elemento mas frecuente:", contador.mas_frecuente())
print("Frecuencia de rojo:", contador.frecuencia_de("rojo"))