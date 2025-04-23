import copy

# -----------------------------
# Clase Prototype base
# -----------------------------
class Prototype:
    def clonar(self):
        return copy.deepcopy(self)


# -----------------------------
# Subclase Avion
# -----------------------------
class Avion(Prototype):
    def __init__(self, body, turbinas, alas, tren_aterrizaje):
        self.body = body
        self.turbinas = turbinas
        self.alas = alas
        self.tren_aterrizaje = tren_aterrizaje

    def mostrar(self):
        print("🛩️ Detalles del avión:")
        print(f"- Body: {self.body}")
        print(f"- Turbinas: {', '.join(self.turbinas)}")
        print(f"- Alas: {', '.join(self.alas)}")
        print(f"- Tren de aterrizaje: {self.tren_aterrizaje}")


# -----------------------------
# Uso: Verificación del clonado
# -----------------------------
if __name__ == "__main__":
    # Crear una instancia de Avion
    avion1 = Avion("Body de avión comercial", ["Turbina A", "Turbina B"], ["Alas principales", "Alas secundarias"], "Tren de aterrizaje")
    avion1.mostrar()

    # Clonar la instancia avion1
    avion_clonado = avion1.clonar()
    avion_clonado.mostrar()

    # Verificar que la clonación es funcional y que es una instancia separada
    print(f"\n¿Son el mismo objeto? {avion1 is avion_clonado}")  # Debe ser False
    print(f"\n¿Son iguales sus atributos? {avion1.body == avion_clonado.body and avion1.tren_aterrizaje == avion_clonado.tren_aterrizaje}")
