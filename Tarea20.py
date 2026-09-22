#   Clase AnalizadorPatrones que: (1) tenga método encontrar_palabras(texto, patron) que busque 
#palabras que inicien con el patrón y retorne una lista; (2) tenga método agrupar_por_longitud(texto) 
#que retorne un diccionario {longitud: [palabras]}; (3) tenga método palabras_unicas() usando un conjunto.
class AnalizadorPatrones:

    def __init__(self):
        self.texto = ""

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        resultado = []

        for palabra in palabras:
            if palabra.startswith(patron):
                resultado.append(palabra)

        return resultado

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        resultado = {}

        for palabra in palabras:
            longitud = len(palabra)

            if longitud not in resultado:
                resultado[longitud] = []

            resultado[longitud].append(palabra)

        return resultado

    def palabras_unicas(self):
        palabras = self.texto.split()

        return set(palabras)


ap = AnalizadorPatrones()

texto = "el gato está aquí el gato"

print("Palabras que empiezan con 'g':",
      ap.encontrar_palabras(texto, "g"))

print("Palabras agrupadas por longitud:",
      ap.agrupar_por_longitud(texto))

ap.texto = texto

print("Palabras unicas:", ap.palabras_unicas())