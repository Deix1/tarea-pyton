#Clase AnalizadorString que: (1) tenga método solo_vocales(letra) que retorne True si es vocal;
#(2) tenga método contar_por_tipo(texto) que retorne un diccionario 
#{'vocales': cant, 'consonantes': cant, 'digitos': cant} reutilizando métodos; (3) tenga atributo 
#que guarde el texto más largo analizado.
class AnalizadorString:

    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, texto):
        for letra in texto:
            if letra not in "aeiouAEIOU":
                return False

        return True

    def contar_por_tipo(self, texto):
        vocales = 0
        consonantes = 0
        numeros = 0

        for letra in texto:
            if letra in "aeiouAEIOU":
                vocales = vocales + 1
            elif letra.isdigit():
                numeros = numeros + 1
            elif letra.isalpha():
                consonantes = consonantes + 1

        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        return {
            "vocales": vocales,
            "consonantes": consonantes,
            "numeros": numeros
        }


analizador = AnalizadorString()

print("Solo vocales:", analizador.solo_vocales("aeiou"))
print("Solo vocales:", analizador.solo_vocales("hola"))

resultado = analizador.contar_por_tipo("Hola Mundo 123")

print("Resultado:", resultado)
print("Texto mas largo:", analizador.texto_mas_largo)