#Clase Calificador que: (1) tenga método validar_nota(nota) que retorne True si 0 ≤ nota ≤ 100,
#False en caso contrario; (2) tenga método cargar_notas(*args) que reciba múltiples notas, 
#las valide, agregue solo las válidas a una lista interna, y retorne esa lista; (3) tenga método promedio()
# que retorne el promedio de notas almacenadas.

class Calificador:

    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        if nota >= 0 and nota <= 100:
            return True
        else:
            return False

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)

    def promedio(self):
        suma = sum(self.notas)
        cantidad = len(self.notas)

        if cantidad > 0:
            return suma / cantidad
        else:
            return 0


calificador = Calificador()

calificador.cargar_notas(85, 92, 78, 88)

print("Notas:", calificador.notas)
print("Promedio:", calificador.promedio())