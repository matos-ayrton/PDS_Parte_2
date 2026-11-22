
import numpy as np
import matplotlib.pyplot as plt

# Parametros da sequencia
a = 0.8
N = 40

# Indices e valores da sequencia
n = np.arange(N)
x = a**n

# Frequencias angulares
omega = np.linspace(-np.pi, np.pi, 1000)

# Pontos da circunferencia unitaria
z = np.exp(1j * omega)

# Transformada-Z numerica
X_numerica = np.zeros(len(omega), dtype=complex)

for indice in range(N):
    X_numerica += x[indice] * z**(-indice)

# Transformada-Z analitica
X_analitica = 1 / (1 - a * z**(-1))

# Magnitude e fase
magnitude = np.abs(X_numerica)
fase = np.angle(X_numerica)

# -------------------------------------------------
# Criacao dos graficos
# -------------------------------------------------

fig, eixos = plt.subplots(3, 1, figsize=(11, 15))

# 1. Sequencia no dominio do tempo
eixos[0].stem(n, x)
eixos[0].set_title("Sequencia exponencial discreta")
eixos[0].set_xlabel("Indice n")
eixos[0].set_ylabel("Amplitude")
eixos[0].grid(True)

# 2. Transformada-Z na circunferencia unitaria
eixos[1].plot(omega, magnitude, label="Magnitude numerica")
eixos[1].plot(
    omega,
    np.abs(X_analitica),
    "--",
    label="Magnitude analitica"
)

eixos[1].set_title("Magnitude da Transformada-Z")
eixos[1].set_xlabel("Frequencia angular (rad/amostra)")
eixos[1].set_ylabel("|X(z)|")
eixos[1].grid(True)
eixos[1].legend()

# 3. Fase da Transformada-Z
eixos[2].plot(omega, fase)
eixos[2].set_title("Fase da Transformada-Z")
eixos[2].set_xlabel("Frequencia angular (rad/amostra)")
eixos[2].set_ylabel("Fase (rad)")
eixos[2].grid(True)

fig.subplots_adjust(hspace=0.65)
plt.show()

# -------------------------------------------------
# Plano-z: polos e zeros
# -------------------------------------------------

fig, ax = plt.subplots(figsize=(9, 7))

# Circunferencia unitaria
angulo = np.linspace(0, 2*np.pi, 500)

ax.plot(
    np.cos(angulo),
    np.sin(angulo),
    linestyle="--",
    label="Circunferencia unitaria"
)

# Polo e zero
ax.scatter(0, 0, marker="o", facecolors="none",
           edgecolors="blue", s=100, label="Zero em z = 0")

ax.scatter(a, 0, marker="x", color="red",
           s=100, label="Polo em z = 0.8")

ax.axhline(0, linewidth=1)
ax.axvline(0, linewidth=1)

ax.set_title("Polos e zeros no plano-z")
ax.set_xlabel("Parte real")
ax.set_ylabel("Parte imaginaria")
ax.set_aspect("equal", adjustable="box")
ax.grid(True)
ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5))
fig.subplots_adjust(right=0.72)

plt.show()
