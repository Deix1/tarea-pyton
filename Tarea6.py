#Clase GestorTemperatura que: (1) tenga método registrar_temperatura(temp) que guarde en una lista; (2) tenga
#método minima()`, `maxima()`, `promedio() que calculen estadísticas; (3) tenga método registrar_multiples
#(*temps) que reutilice el registro para varias temperaturas.
#class AnalizadorNumeros:
class GestorTemperatura:

    def __init__(self):
        self.temperaturas = []

    def registrar(self, temperatura):
        self.temperaturas.append(temperatura)

    def registrar_multiples(self, *temperaturas):
        for temperatura in temperaturas:
            self.registrar(temperatura)

    def temperatura_minima(self):
        return min(self.temperaturas)

    def temperatura_maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        suma = sum(self.temperaturas)
        cantidad = len(self.temperaturas)

        return suma / cantidad


temperatura = GestorTemperatura()

temperatura.registrar_multiples(25, 28, 30, 27, 24)

print("Temperaturas:", temperatura.temperaturas)
print("Temperatura minima:", temperatura.temperatura_minima())
print("Temperatura maxima:", temperatura.temperatura_maxima())
print("Promedio:", temperatura.promedio())