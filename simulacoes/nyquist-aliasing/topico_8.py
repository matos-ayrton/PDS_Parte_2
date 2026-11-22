import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sinal
f0 = 70                  # Frequência original em Hz
fs = 100                 # Frequência de amostragem em Hz
duracao = 0.2            # Duração da observação

# Frequência de Nyquist
f_nyquist = fs / 2

# Cálculo da frequência aparente
f_alias = abs(f0 - fs)

# Sinal contínuo simulado
t_continuo = np.linspace(0, duracao, 5000)
x_continuo = np.cos(2 * np.pi * f0 * t_continuo)

# Sinal de frequência aparente
x_alias_continuo = np.cos(
    2 * np.pi * f_alias * t_continuo
)

# Instantes de amostragem
n = np.arange(0, int(duracao * fs))
t_amostrado = n / fs

# Amostragem do sinal original
x_amostrado = np.cos(
    2 * np.pi * f0 * t_amostrado
)

# Sinal de 30 Hz nos mesmos instantes
x_alias_amostrado = np.cos(
    2 * np.pi * f_alias * t_amostrado
)

# FFT
N = len(x_amostrado)
espectro = np.fft.rfft(x_amostrado)
frequencias = np.fft.rfftfreq(N, d=1/fs)

# Espectro de amplitude
amplitude = np.abs(espectro) / N

if N % 2 == 0:
    amplitude[1:-1] *= 2
else:
    amplitude[1:] *= 2

# Impressão dos resultados
print(f"Frequência original: {f0} Hz")
print(f"Frequência de amostragem: {fs} Hz")
print(f"Frequência de Nyquist: {f_nyquist} Hz")
print(f"Frequência aparente: {f_alias} Hz")

# Criação dos gráficos
fig, eixos = plt.subplots(3, 1, figsize=(12, 15))

# 1. Sinal contínuo
eixos[0].plot(
    t_continuo,
    x_continuo,
    label="Sinal original (70 Hz)"
)

eixos[0].plot(
    t_continuo,
    x_alias_continuo,
    linestyle="--",
    label="Sinal aparente (30 Hz)"
)

eixos[0].set_title("Comparação entre os sinais contínuos")
eixos[0].set_xlabel("Tempo (s)")
eixos[0].set_ylabel("Amplitude")
eixos[0].grid(True)
eixos[0].legend()

# 2. Sinal amostrado
eixos[1].plot(
    t_continuo,
    x_continuo,
    label="Sinal original (70 Hz)"
)

eixos[1].plot(
    t_continuo,
    x_alias_continuo,
    linestyle="--",
    label="Sinal aparente (30 Hz)"
)

eixos[1].stem(
    t_amostrado,
    x_amostrado,
    linefmt="C2-",
    markerfmt="C2o",
    basefmt=" ",
    label="Amostras"
)

eixos[1].set_title("Sequência obtida pela amostragem")
eixos[1].set_xlabel("Tempo (s)")
eixos[1].set_ylabel("Amplitude")
eixos[1].grid(True)
eixos[1].legend()

# 3. Espectro de frequência
eixos[2].stem(frequencias, amplitude)

eixos[2].axvline(
    f_nyquist,
    linestyle="--",
    color="red",
    label="Frequência de Nyquist (50 Hz)"
)

eixos[2].set_title("Espectro do sinal amostrado")
eixos[2].set_xlabel("Frequência (Hz)")
eixos[2].set_ylabel("Amplitude")
eixos[2].set_xlim(0, fs / 2)
eixos[2].grid(True)
eixos[2].legend()

fig.subplots_adjust(hspace=0.65)
plt.show()