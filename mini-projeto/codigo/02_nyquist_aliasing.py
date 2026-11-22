
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# MINI PROJETO - ANÁLISE DE ALIASING
# ==========================================

# Parâmetros do sinal original
A1 = 1.5
A2 = 0.6

f1 = 50
f2 = 120

fase1 = 0
fase2 = np.pi / 4

duracao = 1.0

# Frequências de amostragem
frequencias_amostragem = [1000, 300, 180]

# Sinal contínuo aproximado para visualização
t_continuo = np.linspace(
    0, duracao, 20000, endpoint=False
)

x_continuo = (
    A1 * np.cos(2 * np.pi * f1 * t_continuo + fase1)
    + A2 * np.cos(2 * np.pi * f2 * t_continuo + fase2)
)

# Armazenamento dos resultados
resultados = {}

# ==========================================
# AMOSTRAGEM E FFT
# ==========================================

for fs in frequencias_amostragem:

    Ts = 1 / fs
    N = int(fs * duracao)

    n = np.arange(N)
    t = n * Ts

    # Geração do sinal amostrado
    x = (
        A1 * np.cos(2 * np.pi * f1 * t + fase1)
        + A2 * np.cos(2 * np.pi * f2 * t + fase2)
    )

    # FFT unilateral
    X = np.fft.rfft(x)

    frequencias = np.fft.rfftfreq(N, d=Ts)

    amplitude = np.abs(X) / N

    if N % 2 == 0:
        amplitude[1:-1] *= 2
    else:
        amplitude[1:] *= 2

    # Identificação dos dois maiores picos
    indices_picos = np.argsort(amplitude)[-2:]
    indices_picos = sorted(
        indices_picos,
        key=lambda indice: frequencias[indice]
    )

    # Armazenamento
    resultados[fs] = {
        "t": t,
        "x": x,
        "frequencias": frequencias,
        "amplitude": amplitude,
        "picos": indices_picos
    }

    # Resultados numéricos
    print(f"\n=== AMOSTRAGEM: {fs} Hz ===")
    print(f"Nyquist: {fs / 2:.1f} Hz")
    print(f"Número de amostras: {N}")
    print(f"Resolução: {fs / N:.2f} Hz")

    for indice in indices_picos:
        print(
            f"Frequência observada: "
            f"{frequencias[indice]:.1f} Hz | "
            f"Amplitude: {amplitude[indice]:.4f}"
        )

# ==========================================
# FIGURA 1 - SINAIS E ESPECTROS
# ==========================================

fig, eixos = plt.subplots(
    3, 2,
    figsize=(15, 12),
    constrained_layout=True
)

for i, fs in enumerate(frequencias_amostragem):

    resultado = resultados[fs]

    t = resultado["t"]
    x = resultado["x"]

    frequencias = resultado["frequencias"]
    amplitude = resultado["amplitude"]

    nyquist = fs / 2

    # Gráfico no domínio do tempo
    ax1 = eixos[i, 0]

    intervalo_continuo = t_continuo <= 0.1
    intervalo_amostras = t <= 0.1

    ax1.plot(
        t_continuo[intervalo_continuo],
        x_continuo[intervalo_continuo],
        label="Sinal original",
        linewidth=1.5
    )

    ax1.scatter(
        t[intervalo_amostras],
        x[intervalo_amostras],
        color="red",
        s=22,
        label="Amostras",
        zorder=3
    )

    ax1.set_title(
        f"Amostragem: fs = {fs} Hz"
    )

    ax1.set_xlabel("Tempo (s)")
    ax1.set_ylabel("Amplitude")
    ax1.grid(True)
    ax1.legend()

    # Gráfico do espectro
    ax2 = eixos[i, 1]

    ax2.stem(
        frequencias,
        amplitude
    )

    ax2.axvline(
        nyquist,
        color="red",
        linestyle="--",
        label=f"Nyquist = {nyquist:.0f} Hz"
    )

    ax2.set_title(
        f"Espectro de magnitude - fs = {fs} Hz"
    )

    ax2.set_xlabel("Frequência (Hz)")
    ax2.set_ylabel("Amplitude")

    ax2.set_xlim(0, min(200, nyquist))
    ax2.set_ylim(0, 1.7)

    ax2.grid(True)
    ax2.legend()

plt.show()

# ==========================================
# FIGURA 2 - COMPARAÇÃO DOS ESPECTROS
# ==========================================

fig, eixos = plt.subplots(
    3, 1,
    figsize=(12, 10),
    constrained_layout=True
)

for i, fs in enumerate(frequencias_amostragem):

    resultado = resultados[fs]

    frequencias = resultado["frequencias"]
    amplitude = resultado["amplitude"]

    ax = eixos[i]

    ax.stem(frequencias, amplitude)

    ax.axvline(
        f1,
        color="green",
        linestyle="--",
        label="Componente original: 50 Hz"
    )

    if fs == 180:
        ax.axvline(
            60,
            color="red",
            linestyle="--",
            label="Componente aparente: 60 Hz"
        )
    else:
        ax.axvline(
            f2,
            color="red",
            linestyle="--",
            label="Componente original: 120 Hz"
        )

    ax.set_title(
        f"Comparação espectral - fs = {fs} Hz"
    )

    ax.set_xlabel("Frequência (Hz)")
    ax.set_ylabel("Amplitude")

    ax.set_xlim(0, 160)
    ax.set_ylim(0, 1.7)

    ax.grid(True)
    ax.legend()

plt.show()
