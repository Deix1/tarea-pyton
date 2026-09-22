#Clase SelectorRango que: (1) tenga método crear_rango(inicio, fin) que retorne una tupla con números
#en ese rango; (2) tenga método elementos_en_multiples_rangos(*rangos) que reciba múltiples tuplas
#(inicio,fin) y retorne una lista combinada sin duplicados usando un conjunto.
class SelectorRango:

    def crear_rango(self, inicio, fin):
        numeros = []

        for numero in range(inicio, fin + 1):
            numeros.append(numero)

        return tuple(numeros)

    def elementos_en_multiples_rangos(self, *rangos):
        resultado = set()

        for rango in rangos:
            for numero in rango:
                resultado.add(numero)

        return list(resultado)


selector = SelectorRango()

rango1 = selector.crear_rango(1, 5)
rango2 = selector.crear_rango(4, 8)

print("Rango 1:", rango1)
print("Rango 2:", rango2)

resultado = selector.elementos_en_multiples_rangos(rango1, rango2)

print("Elementos sin repetir:", resultado)