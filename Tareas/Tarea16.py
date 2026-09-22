#Clase CodificadorCesar que: (1) tenga método codificar_letra(letra, desplazamiento) que retorne la letra 
#desplazada en el alfabeto (usar operador %); (2) tenga método codificar_palabra(palabra, desplazamiento) que 
#reutilice para toda la palabra; (3) tenga un diccionario como atributo para historial de codificaciones.
class CodificadorCesar:

    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if letra.isalpha():
            codigo = ord(letra.lower()) - ord("a")
            nuevo_codigo = (codigo + desplazamiento) % 26
            nueva_letra = chr(nuevo_codigo + ord("a"))

            return nueva_letra
        else:
            return letra

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:
            resultado = resultado + self.codificar_letra(letra, desplazamiento)

        self.historial[palabra] = resultado

        return resultado


cc = CodificadorCesar()

print("Letra codificada:", cc.codificar_letra("h", 3))
print("Palabra codificada:", cc.codificar_palabra("hola", 3))
print("Historial:", cc.historial)