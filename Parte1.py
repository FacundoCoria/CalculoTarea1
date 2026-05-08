# Parte 1

import numpy as np
import math
import matplotlib.pyplot as plt

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

        # En la suma inferior se toma el menor valor
        minimo = min(f(x1), f(x2))

        # Área del rectángulo
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

        # En la suma superior se toma el mayor valor
        maximo = max(f(x1), f(x2))

        # Área del rectángulo
        suma += maximo * dx

    return suma


# Parte 2
# Generar tablas comparativas

def generar_tabla(inicio, fin, paso):

    print("\n")
    print(" N    | Suma Inferior | Error Inferior | Suma Superior | Error Superior")
    print("-" * 75)

    for N in range(inicio, fin + 1, paso):

        inf = suma_inferior(N)
        sup = suma_superior(N)

        err_inf = abs(math.pi - inf)
        err_sup = abs(math.pi - sup)

        print(
            f"{N:5d} | "
            f"{inf:14.6f} | "
            f"{err_inf:15.6f} | "
            f"{sup:14.6f} | "
            f"{err_sup:15.6f}"
        )


# Tabla 1
print("\nTABLA 1: N de 10 a 100")
generar_tabla(10, 100, 10)

# Tabla 2
print("\nTABLA 2: N de 100 a 1000")
generar_tabla(100, 1000, 100)

# Tabla 3
print("\nTABLA 3: N de 1000 a 10000")
generar_tabla(1000, 10000, 1000)


# Parte 3
# Gráfico de convergencia

N_vals = list(range(10, 1001, 10))

inf_vals = [suma_inferior(N) for N in N_vals]
sup_vals = [suma_superior(N) for N in N_vals]

plt.plot(N_vals, inf_vals, label="Suma inferior")
plt.plot(N_vals, sup_vals, label="Suma superior")

# Línea horizontal con el valor teórico de π
plt.axhline(y=math.pi, linestyle="--", label="π")

plt.xlabel("N")
plt.ylabel("Aproximación")
plt.title("Convergencia de sumas de Riemann")

plt.legend()

plt.show()