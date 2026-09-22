#Clase RegistroNotas que: (1) tenga método registrar(estudiante, nota) que guarde en un diccionario; 
#(2) tenga método estudiantes_aprobados(nota_minima) que retorne lista de estudiantes; (3) tenga método 
#mejor_estudiante() que retorne nombre y nota del que tiene mayor calificación.
class RegistroNotas:

    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        aprobados = []

        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)

        return aprobados

    def mejor_estudiante(self):
        mejor_nombre = ""
        mejor_nota = 0

        for estudiante, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante

        return (mejor_nombre, mejor_nota)


rn = RegistroNotas()

rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
rn.registrar("Carlos", 85)
rn.registrar("Maria", 60)

print("Notas:", rn.notas)
print("Estudiantes aprobados:", rn.estudiantes_aprobados(70))
print("Mejor estudiante:", rn.mejor_estudiante())