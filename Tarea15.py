#Clase DivisorFinder que: (1) tenga método encontrar_divisores(numero) que retorne una tupla con todos 
#los divisores; (2) tenga método es_perfecto(numero) que retorne True si la suma de sus divisores 
#(excepto él mismo) es igual a él; (3) tenga método encontrar_multiples_divisores(*numeros) que retorne 
#un diccionario {número: tupla_divisores}.
class DivisorFinder:

    def encontrar_divisores(self, numero):
        divisores = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)

        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)

        suma = 0

        for divisor in divisores:
            if divisor != numero:
                suma = suma + divisor

        if suma == numero:
            return True
        else:
            return False

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}

        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)

        return resultado


divisor = DivisorFinder()

print("Divisores de 12:", divisor.encontrar_divisores(12))
print("¿6 es perfecto?:", divisor.es_perfecto(6))

resultado = divisor.encontrar_multiples_divisores(6, 10, 12)

print("Divisores:", resultado)