#Clase Equipos que: (1) tenga método crear_equipo(nombre_equipo) que inicie un equipo como una
#lista vacía en un diccionario; (2) tenga método agregar_jugador(equipo, jugador) que añada el jugador 
#al equipo; (3) tenga método equipo_mayor_integrantes() que retorne el nombre del equipo con más jugadores.
class Equipos:

    def __init__(self):
        self.equipos = {}

    def agregar_jugador(self, equipo, jugador):
        if equipo not in self.equipos:
            self.equipos[equipo] = []

        self.equipos[equipo].append(jugador)

    def equipo_con_mas_jugadores(self):
        equipo_mayor = ""
        mayor = 0

        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > mayor:
                mayor = len(jugadores)
                equipo_mayor = equipo

        return equipo_mayor


equipos = Equipos()

equipos.agregar_jugador("Barcelona", "Juan")
equipos.agregar_jugador("Barcelona", "Pedro")
equipos.agregar_jugador("Barcelona", "Carlos")

equipos.agregar_jugador("Emelec", "Luis")
equipos.agregar_jugador("Emelec", "Ana")

equipos.agregar_jugador("Liga", "Maria")

print("Equipos:", equipos.equipos)
print("Equipo con mas jugadores:", equipos.equipo_con_mas_jugadores())