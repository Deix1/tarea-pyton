#Clase AnalizadorNumeros que: (1) tenga método es_par(numero) que retorne True/False; (2) 
#tenga método separar(*numeros) que retorne un diccionario {'pares': [...], 'impares': [...]} 
#reutilizando es_par; (3) tenga método cantidad_pares_impares() que retorne una tupla (cant_pares, cant_impares).
class AnalizadorNumeros:

    def es_par(self, numero):
        if numero % 2 == 0:
            return True
        else:
            return False

    def separar(self, *numeros):
        resultado = {
            "pares": [],
            "impares": []
        }

        for numero in numeros:
            if self.es_par(numero):
                resultado["pares"].append(numero)
            else:
                resultado["impares"].append(numero)

        return resultado

    def contar(self, *numeros):
        pares = 0
        impares = 0

        for numero in numeros:
            if self.es_par(numero):
                pares = pares + 1
            else:
                impares = impares + 1

        return (pares, impares)


analizador = AnalizadorNumeros()

resultado = analizador.separar(1, 2, 3, 4, 5, 6, 7, 8)

print("Pares:", resultado["pares"])
print("Impares:", resultado["impares"])

cantidad = analizador.contar(1, 2, 3, 4, 5, 6, 7, 8)

print("Cantidad de pares:", cantidad[0])
print("Cantidad de impares:", cantidad[1])