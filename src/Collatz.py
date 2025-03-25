import matplotlib.pyplot as plt

def collatz_iterations(n):
    """Calcula cuántas iteraciones toma para que un número alcance 1 en la conjetura de Collatz."""
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

# Calcular el número de iteraciones para cada número entre 1 y 10000
n_values = list(range(1, 10001))
iterations = [collatz_iterations(n) for n in n_values]

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.scatter(iterations, n_values, s=1, color="blue")  # Gráfico de dispersión
plt.xlabel("Número de iteraciones")
plt.ylabel("Número inicial (n)")
plt.title("Iteraciones necesarias para alcanzar 1 en la conjetura de Collatz")
plt.grid(True)
plt.show()
