
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sinal
N = 64
fs = 64
n = np.arange(N)

# Frequências e amplitudes
f1 = 8
f2 = 16
A1 = 1.5
A2 = 0.75

# Geração do sinal com duas componentes
x = (
    A1 * np.cos(2 * np.pi * f1 * n / fs)
    + A2 * np.cos(2 * np.pi * f2 * n / fs + np.pi / 4)
)

# Cálculo direto da DFT
k = np.arange(N)

X = np.zeros(N, dtype=complex)

for i in range(N):
    X[i] = np.sum(
        x * np.exp(-1j * 2 * np.pi * i * n / N)
    )

# Frequências correspondentes aos coeficientes
frequencias = k * fs / N

# Espectro de magnitude unilateral
magnitude = np.abs(X) / N
magnitude[1:N//2] *= 2

# Espectro de fase
fase = np.angle(X)

# Exibe os coeficientes das frequências principais
print("Coeficientes da DFT:")
for indice in [8, 16, 48, 56]:
    print(
        f"k={indice}, "
        f"frequência={frequencias[indice]:.1f} Hz, "
        f"X[k]={X[indice]:.2f}"
    )

# Gráfico 1: sinal no domínio do tempo
plt.figure(figsize=(10, 4))
plt.stem(n, x)
plt.title("Sinal composto no domínio do tempo")
plt.xlabel("Índice da amostra (n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 2: espectro de magnitude
plt.figure(figsize=(10, 4))
plt.stem(
    frequencias[:N//2 + 1],
    magnitude[:N//2 + 1]
)
plt.title("Espectro de magnitude da DFT")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 3: espectro de fase
frequencias_positivas = frequencias[:N//2 + 1]
fase_positiva = fase[:N//2 + 1]

# Exibe a fase somente onde há componentes relevantes
limite = 0.01
indices_validos = magnitude[:N//2 + 1] > limite

plt.figure(figsize=(10, 4))
plt.stem(
    frequencias_positivas[indices_validos],
    fase_positiva[indices_validos]
)
plt.title("Espectro de fase da DFT")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Fase (rad)")
plt.grid(True)
plt.tight_layout()
plt.show()