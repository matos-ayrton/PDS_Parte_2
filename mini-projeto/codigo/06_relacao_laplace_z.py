
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ==========================================
# MINI-PROJETO - RELACAO ENTRE LAPLACE E Z
# ==========================================

# Pasta para salvar as figuras
pasta_figuras = Path("figuras")
pasta_figuras.mkdir(exist_ok=True)

# Modelo mecanico continuo
# H(s) = 1 / (s^2 + 40s + 10000)

denominador = [1, 40, 10000]

# Polos do sistema continuo
polos_s = np.roots(denominador)

# Periodos de amostragem para comparacao
periodos = [0.001, 0.005, 0.01]

# Circunferencia unitaria
theta = np.linspace(0, 2 * np.pi, 1000)

# ==========================================
# FIGURA 1 - PLANOS S E Z
# ==========================================

fig, eixos = plt.subplots(
    1, 2, figsize=(14, 6), constrained_layout=True
)

# Plano-s
ax = eixos[0]

ax.scatter(
    polos_s.real,
    polos_s.imag,
    color="red",
    marker="x",
    s=130,
    linewidths=2.5,
    label="Polos continuos"
)

ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)

ax.axvspan(
    -40, 0,
    color="green",
    alpha=0.08,
    label="Semiplano estavel"
)

ax.set_xlim(-40, 10)
ax.set_ylim(-120, 120)

ax.set_title("Polos do sistema no plano-s")
ax.set_xlabel("Parte real (sigma)")
ax.set_ylabel("Parte imaginaria (omega)")
ax.grid(True, alpha=0.4)
ax.legend()

# Plano-z
ax = eixos[1]

ax.plot(
    np.cos(theta),
    np.sin(theta),
    "k--",
    label="Circunferencia unitaria"
)

cores = ["blue", "orange", "green"]

for Ts, cor in zip(periodos, cores):

    polos_z = np.exp(polos_s * Ts)

    ax.scatter(
        polos_z.real,
        polos_z.imag,
        color=cor,
        marker="x",
        s=110,
        linewidths=2.5,
        label=f"Ts = {Ts} s"
    )

    print(f"\nPeriodo de amostragem: {Ts} s")
    print(f"Frequencia de amostragem: {1/Ts:.1f} Hz")

    for polo_s, polo_z in zip(polos_s, polos_z):
        print(
            f"s = {polo_s:.4f} -> "
            f"z = {polo_z:.4f} | "
            f"|z| = {abs(polo_z):.4f}"
        )

ax.axhline(0, color="gray", linewidth=0.8)
ax.axvline(0, color="gray", linewidth=0.8)

ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect("equal", adjustable="box")

ax.set_title("Mapeamento dos polos no plano-z")
ax.set_xlabel("Parte real")
ax.set_ylabel("Parte imaginaria")
ax.grid(True, alpha=0.4)
ax.legend(loc="upper left", fontsize=9)

fig.savefig(
    pasta_figuras / "relacao_planos_s_z.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================================
# FIGURA 2 - MODULO E ANGULO DOS POLOS
# ==========================================

# Intervalo de periodos para investigacao
Ts_valores = np.linspace(0.0001, 0.02, 500)

# Escolhemos o polo com parte imaginaria positiva
polo_referencia = polos_s[
    np.argmax(polos_s.imag)
]

# Mapeamento continuo
polos_mapeados = np.exp(
    polo_referencia * Ts_valores
)

modulos = np.abs(polos_mapeados)
angulos = np.angle(polos_mapeados)

fig, eixos = plt.subplots(
    2, 1, figsize=(11, 9), constrained_layout=True
)

# Modulo
eixos[0].plot(
    Ts_valores,
    modulos,
    color="blue",
    linewidth=2
)

eixos[0].axhline(
    1,
    color="red",
    linestyle="--",
    label="Limite de estabilidade |z| = 1"
)

eixos[0].set_title(
    "Variacao do modulo do polo discreto"
)
eixos[0].set_xlabel(
    "Periodo de amostragem Ts (s)"
)
eixos[0].set_ylabel("Modulo |z|")
eixos[0].grid(True)
eixos[0].legend()

# Angulo
eixos[1].plot(
    Ts_valores,
    angulos,
    color="green",
    linewidth=2
)

eixos[1].set_title(
    "Variacao do angulo do polo discreto"
)
eixos[1].set_xlabel(
    "Periodo de amostragem Ts (s)"
)
eixos[1].set_ylabel("Angulo (rad)")
eixos[1].grid(True)

fig.savefig(
    pasta_figuras / "modulo_angulo_polos.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
