
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# =====================================================
# MINI PROJETO - ANÁLISE NO PLANO-S
# Sistema massa-mola-amortecedor
# =====================================================

# Parâmetros físicos
m = 1.0
c = 40.0
k = 10000.0

# Função de transferência H(s) = 1 / (ms² + cs + k)
numerador = [1.0]
denominador = [m, c, k]

sistema = signal.TransferFunction(numerador, denominador)

# Frequência natural e fator de amortecimento
omega_n = np.sqrt(k / m)
f_n = omega_n / (2 * np.pi)
zeta = c / (2 * np.sqrt(m * k))

# Polos e zeros
polos = np.roots(denominador)
zeros = np.roots(numerador)

print("=== PARÂMETROS DO SISTEMA ===")
print(f"Massa: {m} kg")
print(f"Amortecimento: {c} N.s/m")
print(f"Rigidez: {k} N/m")
print(f"Frequência natural: {omega_n:.2f} rad/s")
print(f"Frequência natural: {f_n:.2f} Hz")
print(f"Fator de amortecimento: {zeta:.2f}")
print(f"Polos: {polos}")
print(f"Zeros finitos: {zeros}")

# Intervalo de tempo
tempo = np.linspace(0, 0.5, 2000)

# Resposta ao impulso
t_impulso, y_impulso = signal.impulse(sistema, T=tempo)

# Resposta ao degrau
t_degrau, y_degrau = signal.step(sistema, T=tempo)

# Resposta em frequência
frequencias_hz = np.linspace(0.1, 200, 3000)
omega = 2 * np.pi * frequencias_hz

omega_calculada, resposta = signal.freqresp(sistema, w=omega)

magnitude = np.abs(resposta)

# Frequência aproximada de ressonância
indice_pico = np.argmax(magnitude)
f_ressonancia = frequencias_hz[indice_pico]

print(f"Frequência de ressonância: {f_ressonancia:.2f} Hz")

# =====================================================
# FIGURA 1 - RESPOSTAS TEMPORAIS
# =====================================================

fig1, eixos = plt.subplots(2, 1, figsize=(11, 8))

eixos[0].plot(t_impulso, y_impulso, color="blue")
eixos[0].set_title("Resposta ao impulso do sistema mecânico")
eixos[0].set_xlabel("Tempo (s)")
eixos[0].set_ylabel("Deslocamento (m)")
eixos[0].grid(True)

eixos[1].plot(t_degrau, y_degrau, color="green")
eixos[1].set_title("Resposta ao degrau do sistema mecânico")
eixos[1].set_xlabel("Tempo (s)")
eixos[1].set_ylabel("Deslocamento (m)")
eixos[1].grid(True)

plt.tight_layout()

# =====================================================
# FIGURA 2 - POLOS NO PLANO-S
# =====================================================

fig2, ax = plt.subplots(figsize=(9, 7))

ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)

ax.axvspan(-120, 0, color="green", alpha=0.08,
           label="Semiplano esquerdo (estável)")

ax.axvspan(0, 40, color="red", alpha=0.08,
           label="Semiplano direito (instável)")

ax.scatter(
    polos.real,
    polos.imag,
    marker="x",
    s=150,
    color="red",
    linewidths=2.5,
    label="Polos do sistema"
)

for polo in polos:
    ax.annotate(
        f"{polo.real:.1f} {'+' if polo.imag >= 0 else '-'} "
        f"j{abs(polo.imag):.1f}",
        (polo.real, polo.imag),
        xytext=(10, 8),
        textcoords="offset points"
    )

ax.set_title("Distribuição dos polos no plano-s")
ax.set_xlabel("Parte real (σ)")
ax.set_ylabel("Parte imaginária (ω)")
ax.set_xlim(-120, 40)
ax.set_ylim(-130, 130)
ax.grid(True)
ax.legend(loc="upper left")

plt.tight_layout()

# =====================================================
# FIGURA 3 - RESPOSTA EM FREQUÊNCIA
# =====================================================

fig3, ax = plt.subplots(figsize=(11, 6))

ax.plot(
    frequencias_hz,
    magnitude,
    color="blue",
    label="Magnitude de H(jω)"
)

ax.axvline(
    f_n,
    color="green",
    linestyle="--",
    label=f"Frequência natural = {f_n:.2f} Hz"
)

ax.axvline(
    f_ressonancia,
    color="red",
    linestyle=":",
    label=f"Ressonância ≈ {f_ressonancia:.2f} Hz"
)

ax.set_title("Resposta em frequência do sistema mecânico")
ax.set_xlabel("Frequência (Hz)")
ax.set_ylabel("Magnitude |H(jω)| (m/N)")
ax.grid(True)
ax.legend()

plt.tight_layout()

plt.show()
