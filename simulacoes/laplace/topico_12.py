
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Intervalo de tempo
t = np.linspace(0, 6, 1500)

# Sistemas com diferentes polos
sistemas = {
    "Polo em -1": signal.TransferFunction([1], [1, 1]),
    "Polo em -5": signal.TransferFunction([1], [1, 5]),
    "Polo em +1": signal.TransferFunction([1], [1, -1]),
    "Polos em -1 ± j4": signal.TransferFunction(
        [1], [1, 2, 17]
    )
}

# Sistema com zero em -2
sistema_com_zero = signal.TransferFunction(
    [1, 2], [1, 6, 5]
)

# Sistema de comparação sem zero finito
sistema_sem_zero = signal.TransferFunction(
    [2], [1, 6, 5]
)

# Cálculo das respostas
respostas = {}

for nome, sistema in sistemas.items():
    _, resposta = signal.impulse(sistema, T=t)
    respostas[nome] = resposta

_, resposta_com_zero = signal.impulse(
    sistema_com_zero, T=t
)

_, resposta_sem_zero = signal.impulse(
    sistema_sem_zero, T=t
)

# ==================================================
# FIGURA 1 - RESPOSTAS TEMPORAIS
# ==================================================

fig, eixos = plt.subplots(
    2, 2, figsize=(15, 9), constrained_layout=True
)

# Gráfico 1 - Sistemas estáveis
ax = eixos[0, 0]

for nome in [
    "Polo em -1",
    "Polo em -5",
    "Polos em -1 ± j4"
]:
    ax.plot(t, respostas[nome], label=nome)

ax.set_title("Respostas ao impulso dos sistemas estáveis")
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Amplitude")
ax.grid(True)
ax.legend()

# Gráfico 2 - Sistema instável
ax = eixos[0, 1]

ax.plot(
    t,
    respostas["Polo em +1"],
    color="red",
    label="Polo em +1"
)

ax.set_title("Resposta ao impulso do sistema instável")
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Amplitude")
ax.grid(True)
ax.legend()

# Gráfico 3 - Polos reais negativos
ax = eixos[1, 0]

ax.plot(
    t,
    respostas["Polo em -1"],
    label="Polo em -1"
)

ax.plot(
    t,
    respostas["Polo em -5"],
    label="Polo em -5"
)

ax.set_title("Comparação entre polos reais negativos")
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Amplitude")
ax.grid(True)
ax.legend()

# Gráfico 4 - Polos complexos
ax = eixos[1, 1]

resposta_complexa = respostas["Polos em -1 ± j4"]

ax.plot(
    t,
    resposta_complexa,
    label="Resposta ao impulso"
)

ax.plot(
    t,
    np.exp(-t) / 4,
    "--",
    label="Envoltória superior"
)

ax.plot(
    t,
    -np.exp(-t) / 4,
    "--",
    label="Envoltória inferior"
)

ax.set_title("Resposta com polos complexos conjugados")
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Amplitude")
ax.grid(True)
ax.legend()

plt.show()

# ==================================================
# FIGURA 2 - POLOS E ZEROS NO PLANO-S
# ==================================================

fig, ax = plt.subplots(figsize=(12, 7))

cores = ["C0", "C1", "C2", "C3"]

for (nome, sistema), cor in zip(sistemas.items(), cores):

    polos = np.roots(sistema.den)

    ax.scatter(
        polos.real,
        polos.imag,
        marker="x",
        s=150,
        linewidths=2.5,
        color=cor,
        label=nome,
        zorder=4
    )

# Polos do sistema com zero
polos_zero = np.roots(sistema_com_zero.den)
zeros_zero = np.roots(sistema_com_zero.num)

ax.scatter(
    polos_zero.real,
    polos_zero.imag,
    marker="x",
    s=220,
    linewidths=3,
    color="purple",
    label="Polos do sistema com zero",
    zorder=5
)

ax.scatter(
    zeros_zero.real,
    zeros_zero.imag,
    marker="o",
    s=200,
    facecolors="none",
    edgecolors="purple",
    linewidths=3,
    label="Zero em -2",
    zorder=6
)

# Eixos e regiões
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)

ax.axvspan(-6.5, 0, color="green", alpha=0.06)
ax.axvspan(0, 2, color="red", alpha=0.06)

ax.set_title("Distribuição dos polos e zeros no plano-s")
ax.set_xlabel("Parte real (σ)")
ax.set_ylabel("Parte imaginária (ω)")

ax.set_xlim(-6.5, 2)
ax.set_ylim(-5, 5)

ax.set_aspect("auto")
ax.grid(True, alpha=0.4)

# Legenda fora do gráfico
ax.legend(
    loc="center left",
    bbox_to_anchor=(1.02, 0.5),
    fontsize=10
)

plt.tight_layout()
plt.show()

# ==================================================
# FIGURA 3 - INFLUÊNCIA DE UM ZERO
# ==================================================

fig, ax = plt.subplots(figsize=(11, 5))

ax.plot(
    t,
    resposta_sem_zero,
    linewidth=2,
    label="Sem zero: H(s) = 2/(s² + 6s + 5)"
)

ax.plot(
    t,
    resposta_com_zero,
    linewidth=2,
    label="Com zero: H(s) = (s + 2)/(s² + 6s + 5)"
)

ax.set_title("Influência de um zero na resposta ao impulso")
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Amplitude")
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.show()

# ==================================================
# RESULTADOS NUMÉRICOS
# ==================================================

print("\nANÁLISE DOS POLOS E ZEROS\n")

for nome, sistema in sistemas.items():

    polos = np.roots(sistema.den)
    estavel = np.all(np.real(polos) < 0)

    print(nome)
    print("Polos:", polos)
    print(
        "Estabilidade:",
        "Estável" if estavel else "Instável"
    )
    print()

print("Sistema com zero:")
print("Polos:", np.roots(sistema_com_zero.den))
print("Zeros:", np.roots(sistema_com_zero.num))
