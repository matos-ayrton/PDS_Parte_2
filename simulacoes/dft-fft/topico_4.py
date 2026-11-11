
import numpy as np
import matplotlib.pyplot as plt
import time

# --------------------------------------------------
# 1. Implementação direta da DFT
# --------------------------------------------------
def calcular_dft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)

    for k in range(N):
        soma = 0

        for n in range(N):
            soma += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)

        X[k] = soma

    return X


# --------------------------------------------------
# 2. Geração do sinal
# --------------------------------------------------
N = 64
fs = 64
n = np.arange(N)

x = (
    2 * np.cos(2 * np.pi * 8 * n / fs)
    + np.cos(2 * np.pi * 16 * n / fs)
)


# --------------------------------------------------
# 3. Cálculo pelos dois métodos
# --------------------------------------------------
inicio_dft = time.perf_counter()
X_dft = calcular_dft(x)
tempo_dft = time.perf_counter() - inicio_dft

inicio_fft = time.perf_counter()
X_fft = np.fft.fft(x)
tempo_fft = time.perf_counter() - inicio_fft


# --------------------------------------------------
# 4. Comparação dos coeficientes
# --------------------------------------------------
erro = np.max(np.abs(X_dft - X_fft))

print("COMPARAÇÃO ENTRE DFT E FFT")
print(f"Tempo da DFT direta: {tempo_dft:.8f} segundos")
print(f"Tempo da FFT:        {tempo_fft:.8f} segundos")
print(f"Maior diferença entre os coeficientes: {erro:.12e}")


# --------------------------------------------------
# 5. Gráfico do sinal no domínio do tempo
# --------------------------------------------------
plt.figure(figsize=(10, 4))
plt.stem(n, x)
plt.title("Sinal no domínio do tempo")
plt.xlabel("Amostra (n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 6. Comparação dos espectros
# --------------------------------------------------
frequencias = np.fft.fftfreq(N, d=1/fs)

magnitude_dft = np.abs(X_dft) / N
magnitude_fft = np.abs(X_fft) / N

# Exibição apenas das frequências positivas
metade = N // 2 + 1

plt.figure(figsize=(10, 4))
plt.stem(
    frequencias[:metade],
    magnitude_dft[:metade],
    linefmt='C0-',
    markerfmt='C0o',
    basefmt=' ',
    label='DFT direta'
)
plt.stem(
    frequencias[:metade],
    magnitude_fft[:metade],
    linefmt='C1--',
    markerfmt='C1x',
    basefmt=' ',
    label='FFT'
)
plt.title("Comparação entre os espectros da DFT e da FFT")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 7. Comparação do tempo para diferentes valores de N
# --------------------------------------------------
valores_N = [32, 64, 128, 256, 512, 1024]

tempos_dft = []
tempos_fft = []

for tamanho in valores_N:

    sinal = np.random.rand(tamanho)

    # Mede a DFT direta
    inicio = time.perf_counter()
    calcular_dft(sinal)
    tempos_dft.append(time.perf_counter() - inicio)

    # Mede a FFT
    inicio = time.perf_counter()
    np.fft.fft(sinal)
    tempos_fft.append(time.perf_counter() - inicio)


# --------------------------------------------------
# 8. Gráfico dos tempos de execução
# --------------------------------------------------
plt.figure(figsize=(10, 5))

plt.plot(
    valores_N,
    tempos_dft,
    marker='o',
    label='DFT direta'
)

plt.plot(
    valores_N,
    tempos_fft,
    marker='s',
    label='FFT'
)

plt.title("Comparação do tempo de execução")
plt.xlabel("Número de amostras (N)")
plt.ylabel("Tempo de execução (segundos)")
plt.xscale("log", base=2)
plt.yscale("log")
plt.legend()
plt.grid(True, which="both")
plt.tight_layout()
plt.show()
