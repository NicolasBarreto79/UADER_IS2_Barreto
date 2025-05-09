from abc import ABC, abstractmethod

# Componente base
class NumeroBase(ABC):
    @abstractmethod
    def mostrar(self):
        pass

# Implementación concreta
class Numero(NumeroBase):
    def __init__(self, valor):
        self.valor = valor

    def mostrar(self):
        print(f"Valor: {self.valor}")
        return self.valor

# Decorador base
class OperacionDecorator(NumeroBase):
    def __init__(self, componente: NumeroBase):
        self.componente = componente

# Decorador: Sumar 2
class SumarDos(OperacionDecorator):
    def mostrar(self):
        valor = self.componente.mostrar()
        resultado = valor + 2
        print(f" +2 → {resultado}")
        return resultado

# Decorador: Multiplicar por 2
class MultiplicarPorDos(OperacionDecorator):
    def mostrar(self):
        valor = self.componente.mostrar()
        resultado = valor * 2
        print(f" *2 → {resultado}")
        return resultado

# Decorador: Dividir por 3
class DividirPorTres(OperacionDecorator):
    def mostrar(self):
        valor = self.componente.mostrar()
        resultado = valor / 3
        print(f" /3 → {resultado}")
        return resultado


if __name__ == "__main__":
    print("== Sin decorador ==")
    numero = Numero(9)
    numero.mostrar()

    print("\n== Con operaciones anidadas ==")
    operacion = DividirPorTres(
                    MultiplicarPorDos(
                        SumarDos(
                            Numero(9)
                        )
                    )
                )
    operacion.mostrar()
