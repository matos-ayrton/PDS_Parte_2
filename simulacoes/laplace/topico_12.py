
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Intervalo de tempo
t = np.linspace(0, 6, 1500)

# Sistemas definidos a partir dos polos estudados
sistemas = [
    {
        "nome": "Polo em -1",
        "num": [1],
        "den": [1, 1],
        "polos": [-1]
    },
    {
        "nome": "Polo em -5",
        "num": [1],
        "den": [1, 5],
        "polos": [-5]
    },
    {
        "nome": "Polo em +1",
        "num": [1],
        "den": [1, -1],
        "polos": [1]
    },
    {
        "nome": "Polos em -1 +/- j4",
        "num": [1],
        "den": [1, 2, 17],
        "polos": [-1+4j, -1-4j]
    }
]

fig, eixos = plt.subplots(2, 2, figsize=(13, 9))

# -------------------------------------------------
# 1. Respostas temporais dos quatro sistemas
# -------------------------------------------------

ax = eixos[0, 0]

for sistema in sistemas:
    modelo = signal.TransferFunction(
        sistema["num"],
        sistema["den"]
    )

    tempo, resposta = signal.impulse(modelo, T=t)

    ax.plot(
        tempo,
        resposta,
        label=sistema["nome"]
    )

ax.set_title("Respostas ao impulso")
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Amplitude")
ax.grid(True)
ax.legend()

# -------------------------------------------------
# 2. Comparacao entre os polos reais
# -------------------------------------------------

ax = eixos[0, 1]

for sistema in sistemas[:3]:
    modelo = signal.TransferFunction(
        sistema["num"],
        sistema["den"]
    )

    tempo, resposta = signal.impulse(modelo, T=t)

    ax.plot(
        tempo,
        resposta,
        label=sistema["nome"]
    )

ax.set_title("Comparacao entre polos reais")
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Amplitude")
ax.grid(True)
ax.legend()

# -------------------------------------------------
# 3. Plano-s
# -------------------------------------------------

ax = eixos[1, 0]

for sistema in sistemas:
    polos = sistema["polos"]

    ax.scatter(
        [np.real(p) for p in polos],
        [np.imag(p) for p in polos],
        s=70,
        label=sistema["nome"]
    )

# Eixos de referencia
ax.axhline(0, linewidth=1)
ax.axvline(0, linewidth=1)

# Separacao entre semiplanos
ax.axvspan(-6, 0, alpha=0.08)
ax.axvspan(0, 2, alpha=0.08)

ax.set_title("Distribuicao dos polos no plano-s")
ax.set_xlabel("Parte real - sigma")
ax.set_ylabel("Parte imaginaria - j omega")
ax.grid(True)
ax.legend()

# -------------------------------------------------
# 4. Resposta oscilatoria
# -------------------------------------------------

ax = eixos[1, 1]

modelo = signal.TransferFunction([1], [1, 2, 17])
tempo, resposta = signal.impulse(modelo, T=t)

ax.plot(tempo, resposta, label="Resposta ao impulso")

# Envoltoria teorica
envoltoria = (1/4) * np.exp(-tempo)

ax.plot(
    tempo,
    envoltoria,
    linestyle="--",
    label="Envoltoria superior"
)

ax.plot(
    tempo,
    -envoltoria,
    linestyle="--",
    label="Envoltoria inferior"
)

ax.set_title("Resposta com polos complexos")
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Amplitude")
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.show()
