
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sinal
fs = 1024
N = 256
f0 = 101.3

# Vetor de tempo discreto
n = np.arange(N)
t = n / fs

# Geração da senoide
x = np.cos(2 * np.pi * f0 * t)

# Criação das janelas
janela_retangular = np.ones(N)
janela_hann = np.hanning(N)
janela_hamming = np.hamming(N)

# Aplicação das janelas
sinais = {
    "Retangular": x * janela_retangular,
    "Hann": x * janela_hann,
    "Hamming": x * janela_hamming
}

# FFT com preenchimento de zeros
Nfft = 8192
frequencias = np.fft.rfftfreq(Nfft, d=1/fs)

# Armazenamento dos espectros
espectros_db = {}

for nome, sinal in sinais.items():

    # Cálculo da FFT
    espectro = np.fft.rfft(sinal, n=Nfft)

    # Normalização pela soma dos coeficientes da janela
    ganho = np.sum({
        "Retangular": janela_retangular,
        "Hann": janela_hann,
        "Hamming": janela_hamming
    }[nome])

    amplitude = np.abs(espectro) / ganho

    # Conversão para decibéis
    amplitude_db = 20 * np.log10(
        np.maximum(amplitude / np.max(amplitude), 1e-12)
    )

    espectros_db[nome] = amplitude_db

# Gráfico do sinal original
plt.figure(figsize=(11, 4))
plt.plot(t, x)
plt.title("Sinal original no domínio do tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico das funções janela
plt.figure(figsize=(11, 4))
plt.plot(n, janela_retangular, label="Retangular")
plt.plot(n, janela_hann, label="Hann")
plt.plot(n, janela_hamming, label="Hamming")
plt.title("Comparação entre as funções janela")
plt.xlabel("Amostra")
plt.ylabel("Amplitude da janela")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Comparação dos espectros
plt.figure(figsize=(12, 6))

for nome, amplitude_db in espectros_db.items():
    plt.plot(
        frequencias,
        amplitude_db,
        label=nome
    )

plt.axvline(
    f0,
    linestyle="--",
    label="Frequência original"
)

plt.title("Comparação dos espectros com diferentes janelas")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude relativa (dB)")
plt.xlim(50, 160)
plt.ylim(-100, 5)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Estimativa da frequência pelo maior pico da FFT
print("Frequências estimadas:")

for nome, sinal in sinais.items():

    espectro = np.fft.rfft(sinal, n=Nfft)
    amplitude = np.abs(espectro)

    indice_pico = np.argmax(amplitude)
    frequencia_pico = frequencias[indice_pico]

    print(f"{nome}: {frequencia_pico:.2f} Hz")
