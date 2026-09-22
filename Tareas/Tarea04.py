#Clase InversorSecuencia que: (1) tenga método invertir_lista(lista) que retorne la lista invertida 
#sin usar reversed() (usa manual con bucles); (2) tenga método invertir_multiples(*listas) que reutilice 
#el anterior para invertir varias listas y retorne un diccionario {lista_original: lista_invertida}.
class InversorSecuencia:

    def invertir(self, lista):
        invertida = []

        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])

        return invertida

    def invertir_multiples(self, *listas):
        resultados = {}

        for lista in listas:
            tupla = tuple(lista)
            resultados[tupla] = self.invertir(lista)

        return resultados


inversor = InversorSecuencia()

lista = [1, 2, 3, 4, 5]

print("Lista original:", lista)
print("Lista invertida:", inversor.invertir(lista))

resultado = inversor.invertir_multiples(
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)

print("Varias listas:", resultado)