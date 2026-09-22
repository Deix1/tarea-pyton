#Clase GestorPersonas que: (1) tenga método agregar_persona(nombre, edad) que guarde en un diccionario; 
#(2) tenga método personas_mayores(edad_minima) que retorne una lista de nombres cuya edad sea ≥; (3) 
#tenga método edad_promedio() que retorne el promedio de edades.
class GestorPersonas:

    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def mayores_de(self, edad):
        resultado = []

        for nombre, edad_persona in self.personas.items():
            if edad_persona >= edad:
                resultado.append(nombre)

        return resultado

    def promedio_edad(self):
        suma = 0

        for edad in self.personas.values():
            suma = suma + edad

        if len(self.personas) > 0:
            return suma / len(self.personas)
        else:
            return 0


personas = GestorPersonas()

personas.agregar_persona("Carlos", 20)
personas.agregar_persona("Maria", 17)
personas.agregar_persona("Juan", 25)
personas.agregar_persona("Ana", 19)

print("Personas:", personas.personas)
print("Mayores de 18:", personas.mayores_de(18))
print("Promedio de edad:", personas.promedio_edad())