import numpy as np
import math
import matplotlib.pyplot as plt

# ── Función a integrar ──────────────────────────────────────────────
def f(x):
    return 2 * np.sqrt(1 - x**2)

# ── 1. Generadores de partición ─────────────────────────────────────

def particion_equiespaciada(N):
    return np.linspace(-1, 1, N + 1)

def particion_aleatoria(N):
    puntos_interiores = np.random.uniform(-1, 1, N - 1)
    return np.sort(np.concatenate(([-1.0], puntos_interiores, [1.0])))

def particion_cosenos(N):
    i = np.arange(N + 1)
    pts = np.cos(i * math.pi / N)
    return pts[::-1]  # de -1 a 1

# ── Suma de Riemann (extremo izquierdo) para cualquier partición ────
def suma_riemann(partition):
    xs = partition[:-1]
    dx = np.diff(partition)
    return float(np.sum(f(xs) * dx))

# ── 2. Tablas comparativas ───────────────────────────────────────────

def generar_tabla(inicio, fin, paso, titulo):
    print(f"\n{titulo}")
    header = (
        f"{'N':>6} | "
        f"{'Equiesp.':>12} {'Err. Equiesp.':>14} | "
        f"{'Aleatoria':>12} {'Err. Aleat.':>12} | "
        f"{'Cosenos':>12} {'Err. Cosenos':>13}"
    )
    print(header)
    print("-" * len(header))

    for N in range(inicio, fin + 1, paso):
        eq  = suma_riemann(particion_equiespaciada(N))
        ale = suma_riemann(particion_aleatoria(N))
        cos = suma_riemann(particion_cosenos(N))

        print(
            f"{N:>6} | "
            f"{eq:>12.6f} {abs(eq  - math.pi):>14.6f} | "
            f"{ale:>12.6f} {abs(ale - math.pi):>12.6f} | "
            f"{cos:>12.6f} {abs(cos - math.pi):>13.6f}"
        )

print("TABLA 1: N de 10 a 100")
generar_tabla(10, 100, 10, "TABLA 1: N de 10 a 100 (paso 10)")

print("\nTABLA 2: N de 100 a 1000")
generar_tabla(100, 1000, 100, "TABLA 2: N de 100 a 1000 (paso 100)")

print("\nTABLA 3: N de 1000 a 10000")
generar_tabla(1000, 10000, 1000, "TABLA 3: N de 1000 a 10000 (paso 1000)")

# ── 3. Gráfica de convergencia ───────────────────────────────────────
N_vals = list(range(10, 101, 10)) + list(range(100, 1001, 100)) + list(range(1000, 10001, 1000))

eq_vals, ale_vals, cos_vals = [], [], []
for N in N_vals:
    eq_vals.append(suma_riemann(particion_equiespaciada(N)))
    ale_vals.append(suma_riemann(particion_aleatoria(N)))
    cos_vals.append(suma_riemann(particion_cosenos(N)))

plt.figure(figsize=(10, 5))
plt.plot(N_vals, eq_vals,  label="Equiespaciada", color="steelblue")
plt.plot(N_vals, ale_vals, label="Aleatoria",      color="tomato",   alpha=0.75)
plt.plot(N_vals, cos_vals, label="Cosenos",        color="seagreen")
plt.axhline(math.pi, color="black", linestyle="--", label="π")
plt.xscale("log")
plt.xlabel("N (escala logarítmica)")
plt.ylabel("Aproximación de π")
plt.title("Figura 4 – Convergencia de la integral según tipo de partición")
plt.legend()
plt.tight_layout()
plt.savefig("figura4_convergencia_particiones.png", dpi=150)
plt.show()

# ── 4. Visualización de rectángulos con N=100 ────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(15, 4), sharey=True)

particiones = [
    ("Equiespaciada",  particion_equiespaciada(100)),
    ("Aleatoria",      particion_aleatoria(100)),
    ("Cosenos",        particion_cosenos(100)),
]

x_cont = np.linspace(-1, 1, 500)

for ax, (nombre, pts) in zip(axes, particiones):
    for i in range(len(pts) - 1):
        xi, xf = pts[i], pts[i + 1]
        hi = f(xi)
        ax.bar(
            xi, hi, width=(xf - xi), align="edge",
            color="steelblue", alpha=0.4, edgecolor="steelblue", linewidth=0.2
        )
    ax.plot(x_cont, f(x_cont), color="black", linewidth=1.5, label="f(x)")
    ax.set_title(nombre)
    ax.set_xlabel("x")

axes[0].set_ylabel("f(x)")
fig.suptitle("Figura 5 – Rectángulos de aproximación por tipo de partición (N=100)", fontsize=11)
plt.tight_layout()
plt.savefig("figura5_rectangulos_particiones.png", dpi=150)
plt.show()