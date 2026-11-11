
import numpy as np
import matplotlib.pyplot as plt

# Quantidade de amostras
N = 50
n = np.arange(N)

# Polos reais
polos_reais = [0.5, 0.9, 1.1, -0.8]

# Parametros dos polos complexos
r = 0.85
theta = np.pi / 4

# Armazenamento das respostas
respostas = {}

# -------------------------------------------------
# 1. Sistemas com polos reais
# -------------------------------------------------

for a in polos_reais:
    y = np.zeros(N)

    # Entrada impulso unitario
    x = np.zeros(N)
    x[0] = 1

    for k in range(N):
        if k == 0:
            y[k] = x[k]
        else:
            y[k] = a * y[k-1] + x[k]

    respostas[a] = y

# -------------------------------------------------
# 2. Sistema com polos complexos conjugados
# -------------------------------------------------

y_complexo = np.zeros(N)

x = np.zeros(N)
x[0] = 1

coef1 = 2 * r * np.cos(theta)
coef2 = -(r**2)

for k in range(N):
    if k == 0:
        y_complexo[k] = x[k]
    elif k == 1:
        y_complexo[k] = (
            coef1 * y_complexo[k-1] + x[k]
        )
    else:
        y_complexo[k] = (
            coef1 * y_complexo[k-1]
            + coef2 * y_complexo[k-2]
            + x[k]
        )

respostas["complexo"] = y_complexo

# -------------------------------------------------
# 3. Respostas individuais
# -------------------------------------------------

fig, eixos = plt.subplots(3, 2, figsize=(13, 12))

titulos = [
    "Polo = 0.5",
    "Polo = 0.9",
    "Polo = 1.1",
    "Polo = -0.8",
    "Polos complexos conjugados"
]

chaves = [0.5, 0.9, 1.1, -0.8, "complexo"]

for ax, chave, titulo in zip(
    eixos.flatten(), chaves, titulos
):
    ax.stem(n, respostas[chave])
    ax.set_title(titulo)
    ax.set_xlabel("Indice n")
    ax.set_ylabel("Amplitude")
    ax.grid(True)

# Remove o ultimo quadro vazio
fig.delaxes(eixos[2, 1])

plt.tight_layout()
plt.show()

# -------------------------------------------------
# 4. Comparacao das respostas
# -------------------------------------------------

plt.figure(figsize=(12, 6))

for a in polos_reais:
    plt.plot(
        n,
        respostas[a],
        label=f"Polo = {a}"
    )

plt.plot(
    n,
    respostas["complexo"],
    label="Polos complexos"
)

plt.title("Comparacao das respostas ao impulso")
plt.xlabel("Indice n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()

# -------------------------------------------------
# 5. Representacao dos polos no plano-z
# -------------------------------------------------

fig, ax = plt.subplots(figsize=(8, 8))

# Circulo unitario
angulo = np.linspace(0, 2*np.pi, 500)

ax.plot(
    np.cos(angulo),
    np.sin(angulo),
    linestyle="--",
    label="Circulo unitario"
)

# Eixos
ax.axhline(0, linewidth=1)
ax.axvline(0, linewidth=1)

# Polos reais
for a in polos_reais:
    ax.scatter(
        a, 0,
        marker="x",
        s=100,
        label=f"Polo real: {a}"
    )

# Polos complexos
p1 = r * np.exp(1j * theta)
p2 = r * np.exp(-1j * theta)

ax.scatter(
    p1.real, p1.imag,
    marker="x",
    s=120,
    label="Polo complexo"
)

ax.scatter(
    p2.real, p2.imag,
    marker="x",
    s=120
)

ax.set_title("Estabilidade no plano-z")
ax.set_xlabel("Parte real")
ax.set_ylabel("Parte imaginaria")
ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.3, 1.3)
ax.set_aspect("equal", adjustable="box")
ax.grid(True)
ax.legend()

plt.show()

# -------------------------------------------------
# 6. Classificacao dos sistemas
# -------------------------------------------------

print("CLASSIFICACAO DOS SISTEMAS\n")

for a in polos_reais:
    if abs(a) < 1:
        situacao = "Estavel"
    else:
        situacao = "Instavel"

    print(f"Polo {a:>5}: {situacao}")

print("\nPolos complexos:")
print(f"Modulo dos polos: {abs(p1):.2f}")

if abs(p1) < 1:
    print("Sistema estavel")
else:
    print("Sistema instavel")
