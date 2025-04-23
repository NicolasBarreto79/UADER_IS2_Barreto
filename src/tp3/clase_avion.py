import copy

# -----------------------------
# Avión: La clase que representará un avión
# -----------------------------
class Avion:
    def __init__(self, body=None, turbinas=None, alas=None, tren_aterrizaje=None):
        self.body = body
        self.turbinas = turbinas if turbinas else []
        self.alas = alas if alas else []
        self.tren_aterrizaje = tren_aterrizaje

    def mostrar(self):
        print("🛩️ Detalles del avión:")
        print(f"- Body: {self.body}")
        print(f"- Turbinas: {', '.join(self.turbinas)}")
        print(f"- Alas: {', '.join(self.alas)}")
        print(f"- Tren de aterrizaje: {self.tren_aterrizaje}")


# -----------------------------
# Builder: Construcción del avión paso a paso
# -----------------------------
class AvionBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._body = None
        self._turbinas = []
        self._alas = []
        self._tren_aterrizaje = None

    def agregar_body(self, tipo):
        self._body = tipo
        return self

    def agregar_turbinas(self, turbinas):
        self._turbinas = turbinas
        return self

    def agregar_alas(self, alas):
        self._alas = alas
        return self

    def agregar_tren_aterrizaje(self, tipo):
        self._tren_aterrizaje = tipo
        return self

    def build(self):
        avion = Avion(
            body=self._body,
            turbinas=self._turbinas,
            alas=self._alas,
            tren_aterrizaje=self._tren_aterrizaje
        )
        self.reset()
        return avion


# -----------------------------
# Prototype: Clonación de un avión
# -----------------------------
class AvionPrototype:
    def __init__(self, avion):
        self.avion = avion

    def clonar(self):
        return copy.deepcopy(self.avion)


# -----------------------------
# Uso: Fábrica que construye un avión
# -----------------------------
if __name__ == "__main__":
    # Builder: Construir el avión paso a paso
    builder = AvionBuilder()
    avion = (
        builder
        .agregar_body("Body de avión comercial")
        .agregar_turbinas(["Turbina A", "Turbina B"])
        .agregar_alas(["Alas principales", "Alas secundarias"])
        .agregar_tren_aterrizaje("Tren de aterrizaje con rueda")
        .build()
    )

    avion.mostrar()

    # Prototype: Clonar el avión
    clonador = AvionPrototype(avion)
    avion_clonado = clonador.clonar()
    avion_clonado.mostrar()
