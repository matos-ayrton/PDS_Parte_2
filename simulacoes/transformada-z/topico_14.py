
import numpy as np
import matplotlib.pyplot as plt

# Parametros
a = 0.8
a_bilateral = 0.5
b_bilateral = 0.9
N = 30

# -------------------------------------------------
# 1. Geracao das sequencias
# -------------------------------------------------

# Sequencia causal: x[n] = a^n, para n >= 0
n_causal = np.arange(0, N)
x_causal = a**n_causal

# Sequencia anticausal: x[n] = -a^n, para n < 0
n_anticausal = np.arange(-N, 0)
x_anticausal = -(a**n_anticausal)

# Sequencia bilateral
n_bilateral = np.arange(-N, N + 1)
x_bilateral = np.where(
    n_bilateral >= 0,
    a_bilateral**n_bilateral,
    -(b_bilateral**n_bilateral)
)

# -------------------------------------------------
# 2. Representacao das sequencias
# -------------------------------------------------

fig, eixos = plt.subplots(3, 1, figsize=(10, 14))

eixos[0].stem(n_causal, x_causal)
eixos[0].set_title("Sequencia causal")
eixos[0].set_xlabel("Indice n")
eixos[0].set_ylabel("Amplitude")
eixos[0].grid(True)

eixos[1].stem(n_anticausal, x_anticausal)
eixos[1].set_title("Sequencia anticausal")
eixos[1].set_xlabel("Indice n")
eixos[1].set_ylabel("Amplitude")
eixos[1].grid(True)

eixos[2].stem(n_bilateral, x_bilateral)
eixos[2].set_title("Sequencia bilateral")
eixos[2].set_xlabel("Indice n")
eixos[2].set_ylabel("Amplitude")
eixos[2].grid(True)

fig.subplots_adjust(hspace=0.7)
plt.show()

# -------------------------------------------------
# 3. Representacao das regioes de convergencia
# -------------------------------------------------

fig, eixos = plt.subplots(1, 3, figsize=(16, 5))

limite = 1.5
grade = 400

real = np.linspace(-limite, limite, grade)
imag = np.linspace(-limite, limite, grade)
Re, Im = np.meshgrid(real, imag)

raio = np.sqrt(Re**2 + Im**2)
theta = np.linspace(0, 2*np.pi, 500)

# Caso 1: ROC externa, |z| > 0.8
ax = eixos[0]
ax.contourf(
    Re, Im, (raio > a).astype(float),
    levels=[0.5, 1.5], alpha=0.18
)
ax.add_patch(plt.Circle((0, 0), a, fill=False,
                        linestyle="--", linewidth=2))
ax.scatter(a, 0, marker="x", s=90, label="Polo")
ax.set_title("Causal: |z| > 0.8")
ax.legend()

# Caso 2: ROC interna, |z| < 0.8
ax = eixos[1]
ax.contourf(
    Re, Im, (raio < a).astype(float),
    levels=[0.5, 1.5], alpha=0.18
)
ax.add_patch(plt.Circle((0, 0), a, fill=False,
                        linestyle="--", linewidth=2))
ax.scatter(a, 0, marker="x", s=90, label="Polo")
ax.set_title("Anticausal: |z| < 0.8")
ax.legend()

# Caso 3: ROC anular, 0.5 < |z| < 0.9
ax = eixos[2]
roc_bilateral = (
    (raio > a_bilateral) & (raio < b_bilateral)
)
ax.contourf(
    Re, Im, roc_bilateral.astype(float),
    levels=[0.5, 1.5], alpha=0.18
)
ax.add_patch(plt.Circle((0, 0), a_bilateral,
                        fill=False, linestyle="--"))
ax.add_patch(plt.Circle((0, 0), b_bilateral,
                        fill=False, linestyle="--"))
ax.scatter(a_bilateral, 0, marker="x", s=90,
           label="Polo em 0.5")
ax.scatter(b_bilateral, 0, marker="x", s=90,
           label="Polo em 0.9")
ax.set_title("Bilateral: 0.5 < |z| < 0.9")
ax.legend()

for ax in eixos:
    ax.axhline(0, linewidth=0.8)
    ax.axvline(0, linewidth=0.8)
    ax.set_xlim(-limite, limite)
    ax.set_ylim(-limite, limite)
    ax.set_aspect("equal")
    ax.set_xlabel("Parte real")
    ax.set_ylabel("Parte imaginaria")
    ax.grid(True)

plt.tight_layout()
plt.show()

# -------------------------------------------------
# 4. Teste numerico de convergencia
# -------------------------------------------------

def transformada_causal(z, a, N):
    n = np.arange(N)
    return np.sum((a**n) * (z**(-n)))

def transformada_anticausal(z, a, N):
    n = np.arange(-N, 0)
    return np.sum(-(a**n) * (z**(-n)))

def transformada_bilateral(z, a, b, N):
    n = np.arange(-N, N + 1)
    x = np.where(n >= 0, a**n, -(b**n))
    return np.sum(x * z**(-n))

N_valores = [5, 10, 20, 40, 80]

casos = [
    ("Causal", 1.0, "causal"),
    ("Causal", 0.5, "causal"),
    ("Anticausal", 0.5, "anticausal"),
    ("Anticausal", 1.0, "anticausal"),
    ("Bilateral", 0.7, "bilateral"),
    ("Bilateral", 1.0, "bilateral")
]

for nome, z, tipo in casos:
    print(f"\n{nome} - z = {z}")

    for quantidade in N_valores:
        if tipo == "causal":
            valor = transformada_causal(z, a, quantidade)
        elif tipo == "anticausal":
            valor = transformada_anticausal(z, a, quantidade)
        else:
            valor = transformada_bilateral(
                z, a_bilateral, b_bilateral, quantidade
            )

        print(f"N = {quantidade:2d}: X(z) = {valor:.6f}")
