class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler  # permite el encadenamiento

    def handle(self, number):
        if self.next_handler:
            return self.next_handler.handle(number)
        else:
            print(f"Número {number} no consumido.")


class EvenHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            print(f"EvenHandler consumió el número {number}")
        else:
            super().handle(number)


class PrimeHandler(Handler):
    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def handle(self, number):
        if self.is_prime(number):
            print(f"PrimeHandler consumió el número {number}")
        else:
            super().handle(number)


# --- Ejecución del patrón ---
if __name__ == "__main__":
    prime_handler = PrimeHandler()
    even_handler = EvenHandler()

    # Encadenamiento: primero primos, luego pares
    prime_handler.set_next(even_handler)

    for num in range(1, 101):
        prime_handler.handle(num)
