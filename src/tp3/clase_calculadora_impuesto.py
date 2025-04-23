class CalculadoraImpuestos:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculadoraImpuestos, cls).__new__(cls)
        return cls._instance

    def calcular_total_impuestos(self, base_imponible):
        if base_imponible < 0:
            raise ValueError("La base imponible no puede ser negativa.")
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contribuciones_municipales = base_imponible * 0.012
        total = iva + iibb + contribuciones_municipales
        return total


if __name__ == "__main__":
    ci1 = CalculadoraImpuestos()
    ci2 = CalculadoraImpuestos()

    base = 1000
    total_impuestos = ci1.calcular_total_impuestos(base)
    print(f"Total impuestos sobre ${base} = ${total_impuestos:.2f}")
    print("¿Es la misma instancia?", ci1 is ci2)  # True
