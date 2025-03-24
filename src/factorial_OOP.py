class Factorial:
    def __init__(self):
        pass  # No necesita inicializar atributos

    def calcular_factorial(self, num):
        if num < 0:
            print(f"Factorial de {num} no existe")
            return None
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    def run(self, min_val, max_val):
        if min_val > max_val:
            print("El valor 'min' debe ser menor o igual al valor 'max'")
            return
        
        for num in range(min_val, max_val + 1):
            resultado = self.calcular_factorial(num)
            if resultado is not None:
                print(f"Factorial {num}! es {resultado}")

# Ejemplo de uso
factorial = Factorial()
factorial.run(4, 8)
