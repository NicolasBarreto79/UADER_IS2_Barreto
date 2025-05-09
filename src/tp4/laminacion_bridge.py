from abc import ABC, abstractmethod

# Implementador: Tren Laminador
class TrenLaminador(ABC):
    @abstractmethod
    def laminar(self, largo: float, ancho: float, espesor: float):
        pass

class TrenLaminador5mts(TrenLaminador):
    def laminar(self, largo, ancho, espesor):
        print(f"Laminando plancha de {largo}m x {ancho}m x {espesor}\" en tren de 5 mts")

class TrenLaminador10mts(TrenLaminador):
    def laminar(self, largo, ancho, espesor):
        print(f"Laminando plancha de {largo}m x {ancho}m x {espesor}\" en tren de 10 mts")

# Abstracción: Lámina de Acero
class LaminaAcero:
    def __init__(self, ancho: float, espesor: float, tren: TrenLaminador):
        self.ancho = ancho
        self.espesor = espesor
        self.tren = tren

    def producir(self, largo: float):
        print("Iniciando producción de lámina...")
        self.tren.laminar(largo, self.ancho, self.espesor)


# Crear trenes
tren5 = TrenLaminador5mts()
tren10 = TrenLaminador10mts()

# Crear láminas y asignar trenes
lamina1 = LaminaAcero(ancho=1.5, espesor=0.5, tren=tren5)
lamina2 = LaminaAcero(ancho=1.5, espesor=0.5, tren=tren10)

# Producir láminas
lamina1.producir(largo=5)
lamina2.producir(largo=10)
