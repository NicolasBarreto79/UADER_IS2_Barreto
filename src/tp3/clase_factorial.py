class FactorialCalculator:
    _instance = None  # Variable de clase para almacenar la única instancia

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FactorialCalculator, cls).__new__(cls)
        return cls._instance

    def calcular_factorial(self, n):
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos.")
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado


if __name__ == "__main__":
    fc1 = FactorialCalculator()
    fc2 = FactorialCalculator()

    print("5! =", fc1.calcular_factorial(5))  # 120
    print("¿Es la misma instancia?", fc1 is fc2)  # True
