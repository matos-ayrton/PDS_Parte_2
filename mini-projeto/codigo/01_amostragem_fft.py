
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# MINI PROJETO - MONITORAMENTO DE VIBRAÇÕES
# Etapas 2, 3 e 4
# ==========================================

# Parâmetros das componentes do sinal
A1 = 1.5
A2 = 0.6

f1 = 50
f2 = 120

fase1 = 0
fase2 = np.pi / 4

# Parâmetros de amostragem
fs = 1000
duracao = 1.0

Ts = 1 / fs
N = int(fs * duracao)

# Vetor de tempo discreto
n = np.arange(N)
t = n * Ts

# Sinal de vibração composto
x1 = A1 * np.cos(2 * np.pi * f1 * t + fase1)
x2 = A2 * np.cos(2 * np.pi * f2 * t + fase2)

x = x1 + x2

# Sinal contínuo aproximado para visualização
t_continuo = np.linspace(0, duracao, 10000, endpoint=False)

x_continuo = (
    A1 * np.cos(2 * np.pi * f1 * t_continuo + fase1)
    + A2 * np.cos(2 * np.pi * f2 * t_continuo + fase2)
)

# ==========================================
# ANÁLISE ESPECTRAL
# ==========================================

# FFT unilateral para sinais reais
X = np.fft.rfft(x)

frequencias = np.fft.rfftfreq(N, d=Ts)

# Espectro de amplitude
amplitude = np.abs(X) / N

if N % 2 == 0:
    amplitude[1:-1] *= 2
else:
    amplitude[1:] *= 2

# Espectro de fase
fase = np.angle(X)

# Resolução espectral
resolucao = fs / N

# Identificação das componentes
indice_f1 = np.argmin(np.abs(frequencias - f1))
indice_f2 = np.argmin(np.abs(frequencias - f2))

# Exibir apenas fases de componentes significativas
limiar = 0.01 * np.max(amplitude)

fase_visivel = np.where(amplitude > limiar, fase, np.nan)

# ==========================================
# RESULTADOS NUMÉRICOS
# ==========================================

print("=== PARÂMETROS DA SIMULAÇÃO ===")
print(f"Frequência de amostragem: {fs} Hz")
print(f"Frequência de Nyquist: {fs / 2:.1f} Hz")
print(f"Número de amostras: {N}")
print(f"Período de amostragem: {Ts:.4f} s")
print(f"Duração: {duracao:.2f} s")
print(f"Resolução espectral: {resolucao:.2f} Hz")

print("\n=== COMPONENTES IDENTIFICADAS ===")

for indice in [indice_f1, indice_f2]:
    print(
        f"Frequência: {frequencias[indice]:.1f} Hz | "
        f"Amplitude: {amplitude[indice]:.4f} | "
        f"Fase: {fase[indice]:.4f} rad"
    )

# ==========================================
# GRÁFICO 1 - COMPONENTES INDIVIDUAIS
# ==========================================

plt.figure(figsize=(12, 5))

intervalo = t <= 0.1

plt.plot(t[intervalo], x1[intervalo],
         label="Componente de 50 Hz")

plt.plot(t[intervalo], x2[intervalo],
         label="Componente de 120 Hz")

plt.title("Componentes individuais do sinal de vibração")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude (unidades arbitrárias)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ==========================================
# GRÁFICO 2 - SINAL COMPOSTO E AMOSTRAGEM
# ==========================================

plt.figure(figsize=(12, 5))

intervalo_continuo = t_continuo <= 0.1
intervalo_amostras = t <= 0.1

plt.plot(
    t_continuo[intervalo_continuo],
    x_continuo[intervalo_continuo],
    label="Sinal contínuo aproximado"
)

plt.scatter(
    t[intervalo_amostras],
    x[intervalo_amostras],
    color="red",
    s=18,
    label="Amostras"
)

plt.title("Sinal de vibração composto e sua amostragem")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude (unidades arbitrárias)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ==========================================
# GRÁFICO 3 - ESPECTRO DE MAGNITUDE
# ==========================================

plt.figure(figsize=(12, 5))

plt.stem(frequencias, amplitude)

plt.axvline(
    f1, color="red", linestyle="--",
    label=f"Componente de {f1} Hz"
)

plt.axvline(
    f2, color="green", linestyle="--",
    label=f"Componente de {f2} Hz"
)

plt.title("Espectro de magnitude do sinal de vibração")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Amplitude")
plt.xlim(0, 200)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ==========================================
# GRÁFICO 4 - ESPECTRO DE FASE
# ==========================================

plt.figure(figsize=(12, 5))

plt.stem(frequencias, fase_visivel)

plt.title("Espectro de fase do sinal de vibração")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Fase (rad)")
plt.xlim(0, 200)
plt.ylim(-np.pi, np.pi)
plt.grid(True)
plt.tight_layout()
plt.show()
