import os

#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state con memorias
#*--------------------------------------------------------------------

"""State class: Base State class"""
class State:

    def scan(self):
        # Recorremos primero las memorias
        if self.pos_mem < len(self.radio.memories):
            mem_label, mem_type, mem_freq = self.radio.memories[self.pos_mem]
            print(f"Sintonizando memoria {mem_label}: {mem_freq} ({mem_type})")
            self.pos_mem += 1
        else:
            # Recorremos las estaciones normales
            self.pos_station += 1
            if self.pos_station == len(self.stations):
                self.pos_station = 0
                self.pos_mem = 0  # Reinicia las memorias al siguiente ciclo
            print("Sintonizando... Estación {} {}".format(self.stations[self.pos_station], self.name))

#*------- Implementa cómo barrer las estaciones de AM
class AmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.name = "AM"
        self.pos_station = 0
        self.pos_mem = 0

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

#*------- Implementa cómo barrer las estaciones de FM
class FmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.name = "FM"
        self.pos_station = 0
        self.pos_mem = 0

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

#*--------- Construye la radio con todas sus formas de sintonía
class Radio:

    def __init__(self):
        # Lista de memorias compartida
        # Cada memoria es una tupla: (etiqueta, tipo, frecuencia)
        self.memories = [
            ("M1", "AM", "1250"),
            ("M2", "FM", "89.1"),
            ("M3", "FM", "103.9"),
            ("M4", "AM", "1380")
        ]

        self.fmstate = FmState(self)
        self.amstate = AmState(self)

        # Inicialmente en FM
        self.state = self.fmstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

#*---------------------

if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()

    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
    actions *= 2

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado\n")
    for action in actions:
        action()
