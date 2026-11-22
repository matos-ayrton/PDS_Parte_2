
import numpy as np
import matplotlib.pyplot as plt

# Valores dos polos propostos pelo professor
polos = [0.5, 0.9, 1.1, -0.8]

# Quantidade de amostras
N = 25
n = np.arange(N)

# Impulso unitario
x = np.zeros(N)
x[0] = 1

# Armazenamento das respostas
respostas = {}

# -------------------------------------------------
# 1. Calculo das respostas ao impulso
# -------------------------------------------------

for a in polos:
    y = np.zeros(N)

    for k in range(N):
        if k == 0:
            y[k] = x[k]
        else:
            y[k] = a * y[k-1] + x[k]

    respostas[a] = y

# -------------------------------------------------
# 2. Grafico das respostas ao impulso
# -------------------------------------------------

fig, eixos = plt.subplots(2, 2, figsize=(12, 8))

for ax, a in zip(eixos.flatten(), polos):
    ax.stem(n, respostas[a])
    ax.set_title(f"Resposta ao impulso - Polo a = {a}")
    ax.set_xlabel("Indice n")
    ax.set_ylabel("Amplitude")
    ax.grid(True)

plt.tight_layout()
plt.show()

# -------------------------------------------------
# 3. Comparacao das respostas
# -------------------------------------------------

plt.figure(figsize=(11, 6))

for a in polos:
    plt.plot(
        n,
        respostas[a],
        marker="o",
        markersize=3,
        label=f"Polo = {a}"
    )

plt.title("Comparacao das respostas ao impulso")
plt.xlabel("Indice n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()

# -------------------------------------------------
# 4. Representacao dos polos e zeros no plano-z
# -------------------------------------------------

fig, ax = plt.subplots(figsize=(11, 8))

# Circunferencia unitaria
theta = np.linspace(0, 2*np.pi, 500)

ax.plot(
    np.cos(theta),
    np.sin(theta),
    linestyle="--",
    label="Circunferencia unitaria"
)

# Eixos do plano complexo
ax.axhline(0, linewidth=1)
ax.axvline(0, linewidth=1)

# Polos e zeros
for a in polos:
    ax.scatter(
        a, 0,
        marker="x",
        s=100,
        label=f"Polo em z = {a}"
    )

# Zero na origem, comum aos sistemas
ax.scatter(
    0, 0,
    marker="o",
    facecolors="none",
    edgecolors="black",
    s=120,
    label="Zero em z = 0"
)

ax.set_title("Polos e zeros no plano-z")
ax.set_xlabel("Parte real")
ax.set_ylabel("Parte imaginaria")
ax.set_xlim(-1.4, 1.4)
ax.set_ylim(-1.4, 1.4)
ax.set_aspect("equal", adjustable="box")
ax.grid(True)
ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5))
fig.subplots_adjust(right=0.68)

plt.show()

# -------------------------------------------------
# 5. Impressao dos primeiros valores
# -------------------------------------------------

for a in polos:
    print(f"\nPolo: {a}")
    print("Primeiras amostras:", np.round(respostas[a][:10], 5))

    if abs(a) < 1:
        print("Classificacao: estavel (BIBO)")
    else:
        print("Classificacao: instavel (BIBO)")
