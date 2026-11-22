
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sinal
fs = 1024
f1 = 50
f2 = 55

# Quantidades de amostras analisadas
valores_N = [64, 256, 1024]

# Geração e análise do sinal
fig, axs = plt.subplots(3, 1, figsize=(12, 15), constrained_layout=True)

for i, N in enumerate(valores_N):

    # Vetor de tempo
    t = np.arange(N) / fs

    # Sinal composto por duas senoides
    x = (
        np.cos(2 * np.pi * f1 * t)
        + 0.8 * np.cos(2 * np.pi * f2 * t)
    )

    # Cálculo da FFT
    X = np.fft.fft(x)

    # Espectro de magnitude unilateral
    frequencias = np.fft.rfftfreq(N, d=1/fs)
    magnitude = np.abs(X[:N//2 + 1]) / N

    # Correção da amplitude do espectro unilateral
    if N % 2 == 0:
        magnitude[1:-1] *= 2
    else:
        magnitude[1:] *= 2

    # Resolução espectral
    delta_f = fs / N

    # Gráfico
    axs[i].stem(frequencias, magnitude)

    axs[i].set_title(
        f"N = {N} | Resolução = {delta_f:.2f} Hz"
    )

    axs[i].set_xlabel("Frequência (Hz)")
    axs[i].set_ylabel("Magnitude")
    axs[i].set_xlim(35, 70)
    axs[i].grid(True)

plt.show()

# Apresentação dos valores calculados
print("Comparação da resolução espectral")

for N in valores_N:
    delta_f = fs / N
    duracao = N / fs

    print(
        f"N = {N:4d} | "
        f"Resolução = {delta_f:6.2f} Hz | "
        f"Duração = {duracao:.4f} s"
    )
