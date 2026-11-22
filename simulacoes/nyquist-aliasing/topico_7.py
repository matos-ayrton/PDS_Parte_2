
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sinal original
f0 = 100                  # Frequência do sinal em Hz
duracao = 0.2             # Duração da observação em segundos

# Sinal contínuo aproximado para visualização
t_continuo = np.linspace(0, duracao, 5000)
x_continuo = np.cos(2 * np.pi * f0 * t_continuo)

# Frequências de amostragem analisadas
frequencias_amostragem = [500, 200, 150]

fig, eixos = plt.subplots(
    3, 2, figsize=(14, 15), constrained_layout=True
)

for i, fs in enumerate(frequencias_amostragem):

    # Geração das amostras
    Ts = 1 / fs
    N = int(duracao * fs)

    n = np.arange(N)
    t_amostrado = n * Ts

    x_amostrado = np.cos(2 * np.pi * f0 * t_amostrado)

    # Frequência de Nyquist
    f_nyquist = fs / 2

    # FFT unilateral para sinais reais
    espectro = np.fft.rfft(x_amostrado)
    frequencias_positivas = np.fft.rfftfreq(N, d=Ts)

    # Normalização do espectro de amplitude
    amplitude = np.abs(espectro) / N

    # Duplicar apenas as componentes internas
    # DC e Nyquist não devem ser duplicadas
    if N % 2 == 0:
        amplitude[1:-1] *= 2
    else:
        amplitude[1:] *= 2

    # Identificação da maior componente espectral
    indice_pico = np.argmax(amplitude)
    frequencia_observada = frequencias_positivas[indice_pico]

    # Exibição dos resultados no terminal
    print(f"\nFrequência de amostragem: {fs} Hz")
    print(f"Frequência de Nyquist: {f_nyquist:.1f} Hz")
    print(f"Frequência observada: {frequencia_observada:.1f} Hz")
    print(f"Amplitude observada: {amplitude[indice_pico]:.4f}")

    # Gráfico do sinal no domínio do tempo
    ax1 = eixos[i, 0]

    ax1.plot(
        t_continuo,
        x_continuo,
        label="Sinal contínuo"
    )

    ax1.stem(
        t_amostrado,
        x_amostrado,
        linefmt="C1-",
        markerfmt="C1o",
        basefmt=" ",
        label="Amostras"
    )

    ax1.set_title(
        f"Amostragem: fs = {fs} Hz | Nyquist = {f_nyquist:.1f} Hz"
    )
    ax1.set_xlabel("Tempo (s)")
    ax1.set_ylabel("Amplitude")
    ax1.set_xlim(0, duracao)
    ax1.grid(True)
    ax1.legend()

    # Gráfico do espectro
    ax2 = eixos[i, 1]

    ax2.stem(
        frequencias_positivas,
        amplitude
    )

    ax2.axvline(
        f_nyquist,
        linestyle="--",
        color="red",
        label="Frequência de Nyquist"
    )

    ax2.set_title(
        f"Espectro | Frequência observada: {frequencia_observada:.1f} Hz"
    )
    ax2.set_xlabel("Frequência (Hz)")
    ax2.set_ylabel("Amplitude")
    ax2.set_xlim(0, f_nyquist)
    ax2.set_ylim(0, 1.15)
    ax2.grid(True)
    ax2.legend()

plt.show()
