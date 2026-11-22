
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# -------------------------------------------------
# 1. Funcao de transferencia
# H(z) = (1 - 0.7z^-1) / (1 + 0.81z^-2)
# -------------------------------------------------

b = [1, -0.7]
a = [1, 0, 0.81]

# -------------------------------------------------
# 2. Calculo da resposta em frequencia
# -------------------------------------------------

w, H = freqz(b, a, worN=2048)

magnitude = np.abs(H)
fase = np.angle(H)

# -------------------------------------------------
# 3. Identificacao de polos e zeros
# -------------------------------------------------

zeros = np.roots(b)
polos = np.roots(a)

print("Zeros:")
for z in zeros:
    print(z)

print("\nPolos:")
for p in polos:
    print(p)

# -------------------------------------------------
# 4. Diagrama de polos e zeros
# -------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 8))

angulo = np.linspace(0, 2*np.pi, 500)

# Circulo unitario
ax.plot(
    np.cos(angulo),
    np.sin(angulo),
    linestyle="--",
    label="Circulo unitario"
)

# Eixos
ax.axhline(0, linewidth=1)
ax.axvline(0, linewidth=1)

# Zeros
ax.scatter(
    zeros.real,
    zeros.imag,
    marker="o",
    facecolors="none",
    edgecolors="blue",
    s=120,
    label="Zeros"
)

# Polos
ax.scatter(
    polos.real,
    polos.imag,
    marker="x",
    color="red",
    s=120,
    label="Polos"
)

ax.set_title("Polos e zeros no plano-z")
ax.set_xlabel("Parte real")
ax.set_ylabel("Parte imaginaria")
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect("equal", adjustable="box")
ax.grid(True)
ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5))
fig.subplots_adjust(right=0.72)

plt.show()

# -------------------------------------------------
# 5. Magnitude da resposta em frequencia
# -------------------------------------------------

plt.figure(figsize=(11, 5))

plt.plot(w / np.pi, magnitude)

plt.title("Magnitude da resposta em frequencia")
plt.xlabel("Frequencia normalizada (x pi rad/amostra)")
plt.ylabel("|H(e^jw)|")
plt.grid(True)

plt.show()

# -------------------------------------------------
# 6. Fase da resposta em frequencia
# -------------------------------------------------

plt.figure(figsize=(11, 5))

plt.plot(w / np.pi, fase)

plt.title("Fase da resposta em frequencia")
plt.xlabel("Frequencia normalizada (x pi rad/amostra)")
plt.ylabel("Fase (rad)")
plt.grid(True)

plt.show()

# -------------------------------------------------
# 7. Identificacao de valores importantes
# -------------------------------------------------

indice_maximo = np.argmax(magnitude)
indice_minimo = np.argmin(magnitude)

print("\nResultados da resposta em frequencia:")

print(
    f"Maior magnitude: {magnitude[indice_maximo]:.4f}"
)

print(
    f"Frequencia do maior valor: "
    f"{w[indice_maximo]:.4f} rad/amostra"
)

print(
    f"Menor magnitude: {magnitude[indice_minimo]:.4f}"
)

print(
    f"Frequencia do menor valor: "
    f"{w[indice_minimo]:.4f} rad/amostra"
)

# -------------------------------------------------
# 8. Verificacao da estabilidade
# -------------------------------------------------

print("\nVerificacao dos polos:")

for p in polos:
    print(
        f"Polo: {p:.4f} | Modulo: {abs(p):.4f}"
    )

if all(abs(p) < 1 for p in polos):
    print("Sistema estavel.")
else:
    print("Sistema instavel.")
