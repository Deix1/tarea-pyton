#Clase Tareas que: (1) tenga método agregar_tarea(descripcion, prioridad) 
#que guarde en una lista de tuplas (descripción, prioridad); (2) tenga método tareas_prioritarias() que 
#retorne solo las de prioridad alta; (3) tenga método eliminar_completada(descripcion) que borre la tarea 
#de la lista.
class Tareas:

    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        tarea = (descripcion, prioridad)
        self.tareas.append(tarea)

    def tareas_alta_prioridad(self):
        resultado = []

        for tarea in self.tareas:
            if tarea[1] == "alta":
                resultado.append(tarea)

        return resultado

    def eliminar_tarea(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                return True

        return False


tareas = Tareas()

tareas.agregar_tarea("Hacer tarea de Python", "alta")
tareas.agregar_tarea("Estudiar matematicas", "media")
tareas.agregar_tarea("Ordenar el cuarto", "baja")
tareas.agregar_tarea("Hacer ejercicio", "alta")

print("Tareas:", tareas.tareas)
print("Tareas de alta prioridad:", tareas.tareas_alta_prioridad())

tareas.eliminar_tarea("Ordenar el cuarto")

print("Tareas despues de eliminar:", tareas.tareas)