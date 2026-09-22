#Clase CalculadorDistancia que: (1) tenga método distancia_euclidiana(p1, p2) que reciba dos tuplas 
#(x,y) y calcule la distancia; (2) tenga método punto_mas_cercano(referencia, *puntos) que retorne el 
#punto más cercano a referencia; (3) tenga un atributo lista para guardar todas las distancias calculadas.
import math


class CalculadorDistancia:

    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]

        x2 = p2[0]
        y2 = p2[1]

        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        punto_cercano = None
        distancia_menor = None

        for punto in puntos:
            distancia = self.distancia_euclidiana(referencia, punto)

            if distancia_menor is None or distancia < distancia_menor:
                distancia_menor = distancia
                punto_cercano = punto

        return punto_cercano


cd = CalculadorDistancia()

print("Distancia:", cd.distancia_euclidiana((0, 0), (3, 4)))

resultado = cd.punto_mas_cercano(
    (0, 0),
    (3, 4),
    (1, 1),
    (5, 2)
)

print("Punto mas cercano:", resultado)
print("Distancias:", cd.distancias)
