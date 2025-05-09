from abc import ABC, abstractmethod

# Componente base
class Componente(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def mostrar(self, nivel=0):
        pass

# Hoja: Pieza individual
class Pieza(Componente):
    def mostrar(self, nivel=0):
        print("  " * nivel + f"Pieza: {self.nombre}")

# Composite: Subconjunto o ensamblado
class SubConjunto(Componente):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.componentes = []

    def agregar(self, componente: Componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"SubConjunto: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar(nivel + 1)


if __name__ == "__main__":
    # Producto principal
    producto = SubConjunto("Producto Principal")

    # Crear 3 subconjuntos con 4 piezas cada uno
    for i in range(1, 4):
        subconjunto = SubConjunto(f"SubConjunto {i}")
        for j in range(1, 5):
            subconjunto.agregar(Pieza(f"Pieza {i}.{j}"))
        producto.agregar(subconjunto)

    # Mostrar estructura inicial
    print("Estructura inicial:")
    producto.mostrar()

    # Agregar subconjunto adicional opcional
    subconjunto_extra = SubConjunto("SubConjunto Extra")
    for k in range(1, 5):
        subconjunto_extra.agregar(Pieza(f"Pieza Extra.{k}"))
    producto.agregar(subconjunto_extra)

    # Mostrar estructura con subconjunto adicional
    print("\nEstructura con subconjunto adicional:")
    producto.mostrar()
