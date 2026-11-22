
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# MINI PROJETO - ANÁLISE DE JANELAMENTO
# ==========================================

# Parâmetros do sinal
A1 = 1.5
A2 = 0.6

f1 = 50
f2 = 120

fase1 = 0
fase2 = np.pi / 4

# Parâmetros de amostragem
fs = 1000
N = 256

Ts = 1 / fs
duracao = N / fs

n = np.arange(N)
t = n * Ts

# Geração do sinal composto
x = (
    A1 * np.cos(2 * np.pi * f1 * t + fase1)
    + A2 * np.cos(2 * np.pi * f2 * t + fase2)
)

# ==========================================
# FUNÇÕES JANELA
# ==========================================

janelas = {
    "Retangular": np.ones(N),
    "Hann": np.hanning(N),
    "Hamming": np.hamming(N)
}

# Aplicação das janelas
sinais_janelados = {}

for nome, janela in janelas.items():
    sinais_janelados[nome] = x * janela

# ==========================================
# CÁLCULO DOS ESPECTROS
# ==========================================

N_fft = 8192

frequencias = np.fft.rfftfreq(
    N_fft,
    d=Ts
)

espectros = {}
espectros_db = {}

for nome, janela in janelas.items():

    sinal_janelado = sinais_janelados[nome]

    # FFT com zero-padding
    X = np.fft.rfft(
        sinal_janelado,
        n=N_fft
    )

    # Correção pelo ganho coerente da janela
    amplitude = np.abs(X) / np.sum(janela)

    # Espectro unilateral
    if N_fft % 2 == 0:
        amplitude[1:-1] *= 2
    else:
        amplitude[1:] *= 2

    espectros[nome] = amplitude

    # Conversão para decibéis
    referencia = np.max(amplitude)

    amplitude_db = 20 * np.log10(
        np.maximum(
            amplitude / referencia,
            1e-10
        )
    )

    espectros_db[nome] = amplitude_db

# ==========================================
# RESULTADOS NUMÉRICOS
# ==========================================

print("=== PARÂMETROS DA SIMULAÇÃO ===")

print(f"Frequência de amostragem: {fs} Hz")
print(f"Número de amostras: {N}")
print(f"Duração: {duracao:.4f} s")
print(f"Resolução espectral: {fs / N:.4f} Hz")

print("\n=== GANHO COERENTE DAS JANELAS ===")

for nome, janela in janelas.items():

    ganho = np.sum(janela) / N

    print(
        f"{nome}: {ganho:.6f}"
    )

# ==========================================
# FIGURA 1 - SINAL ORIGINAL
# ==========================================

plt.figure(figsize=(12, 5))

plt.plot(
    t,
    x,
    label="Sinal de vibração"
)

plt.title(
    "Sinal de vibração no intervalo de observação"
)

plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude (unidades arbitrárias)")

plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ==========================================
# FIGURA 2 - COMPARAÇÃO DAS JANELAS
# ==========================================

plt.figure(figsize=(12, 5))

for nome, janela in janelas.items():

    plt.plot(
        n,
        janela,
        label=nome
    )

plt.title("Comparação entre as funções janela")

plt.xlabel("Índice da amostra (n)")
plt.ylabel("Coeficiente da janela")

plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ==========================================
# FIGURA 3 - ESPECTRO EM ESCALA LINEAR
# ==========================================

plt.figure(figsize=(12, 5))

for nome, amplitude in espectros.items():

    plt.plot(
        frequencias,
        amplitude,
        label=nome
    )

plt.axvline(
    f1,
    color="black",
    linestyle="--",
    alpha=0.6,
    label="50 Hz"
)

plt.axvline(
    f2,
    color="gray",
    linestyle="--",
    alpha=0.6,
    label="120 Hz"
)

plt.title(
    "Comparação dos espectros de magnitude"
)

plt.xlabel("Frequência (Hz)")
plt.ylabel("Amplitude")

plt.xlim(0, 180)

plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ==========================================
# FIGURA 4 - ESPECTRO EM DECIBÉIS
# ==========================================

plt.figure(figsize=(12, 6))

for nome, amplitude_db in espectros_db.items():

    plt.plot(
        frequencias,
        amplitude_db,
        label=nome
    )

plt.axvline(
    f1,
    color="black",
    linestyle="--",
    alpha=0.6,
    label="50 Hz"
)

plt.axvline(
    f2,
    color="gray",
    linestyle="--",
    alpha=0.6,
    label="120 Hz"
)

plt.title(
    "Comparação espectral com diferentes janelas"
)

plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude relativa (dB)")

plt.xlim(0, 180)
plt.ylim(-100, 5)

plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
