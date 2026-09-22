#Clase AgrupadorEdades que: (1) tenga método clasificar_edad(edad) que retorne la categoría 
#("niño", "adolescente", "adulto", "mayor"); (2) tenga método agrupar_por_categoria(*edades) 
#que retorne un diccionario con {categoría: [edades]}; (3) tenga método edad_promedio_categoria(categoria).
class AgrupadorEdades:

    def __init__(self):
        self.edades = {}

    def clasificar_edad(self, edad):
        if edad <= 12:
            return "niño"
        elif edad <= 17:
            return "adolescente"
        elif edad <= 64:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        resultado = {}

        for edad in edades:
            categoria = self.clasificar_edad(edad)

            if categoria not in resultado:
                resultado[categoria] = []

            resultado[categoria].append(edad)

        self.edades = resultado

        return resultado

    def edad_promedio_categoria(self, categoria):
        if categoria not in self.edades:
            return 0

        edades = self.edades[categoria]

        suma = sum(edades)

        return suma / len(edades)


agrupador = AgrupadorEdades()

resultado = agrupador.agrupar_por_categoria(
    8, 12, 15, 17, 20, 25, 40, 70
)

print("Edades agrupadas:", resultado)

print("Promedio de adultos:",
      agrupador.edad_promedio_categoria("adulto"))