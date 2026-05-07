# Parte 1

import numpy as np
import math

# Definimos la función
def f(x):
    return 2 * np.sqrt(1 - x**2)

# Calcular la suma inferior
def suma_inferior(N):
    a, b = -1, 1
    dx = (b - a) / N
    suma = 0

    for i in range(N):
        x1 = a + i * dx
        x2 = a + (i + 1) * dx
        
        # mínimo en los extremos
        minimo = min(f(x1), f(x2))
        suma += minimo * dx

    return suma

# Calcular la suma superior
def suma_superior(N):
    a, b = -1, 1
    dx = (b - a) / N
    suma = 0

    for i in range(N):
        x1 = a + i * dx
        x2 = a + (i + 1) * dx
        
        # máximo en los extremos
        maximo = max(f(x1), f(x2))
        suma += maximo * dx

    return suma

# Parte 2
# Se genera la tabla con los datos de: N, suma inferior y superior, error inferior y superior.
def generar_tabla(inicio, fin, paso):
    print("N | Suma Inf | Error Inf | Suma Sup | Error Sup")
    print("-" * 60)

    for N in range(inicio, fin + 1, paso):
        inf = suma_inferior(N)
        sup = suma_superior(N)

        err_inf = abs(math.pi - inf)
        err_sup = abs(math.pi - sup)

        print(f"{N:5d} | {inf:.6f} | {err_inf:.6f} | {sup:.6f} | {err_sup:.6f}")

# Tabla 1
generar_tabla(10, 100, 10)

# Tabla 2
generar_tabla(100, 1000, 100)

# Tabla 3
generar_tabla(1000, 10000, 1000)

# Parte 3
# Se genera el gráfico de aproximaciones de la integral según aumenta N.
import matplotlib.pyplot as plt

N_vals = list(range(10, 1001, 10))

inf_vals = [suma_inferior(N) for N in N_vals]
sup_vals = [suma_superior(N) for N in N_vals]

plt.plot(N_vals, inf_vals, label="Suma inferior")
plt.plot(N_vals, sup_vals, label="Suma superior")
plt.axhline(y=math.pi, linestyle="--", label="π")

plt.xlabel("N")
plt.ylabel("Aproximación")
plt.title("Convergencia de sumas de Riemann")
plt.legend()

plt.show()