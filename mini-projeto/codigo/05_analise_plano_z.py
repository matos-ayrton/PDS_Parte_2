
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# =====================================================
# MINI PROJETO - ANÁLISE NO PLANO-Z
# Discretização do sistema massa-mola-amortecedor
# =====================================================

# Parâmetros do sistema mecânico
m = 1.0
c = 40.0
k = 10000.0

# Frequência e período de amostragem
fs = 1000.0
Ts = 1 / fs

# Sistema contínuo H(s)
num_s = [1.0]
den_s = [m, c, k]

sistema_continuo = signal.TransferFunction(num_s, den_s)

# Discretização pelo método ZOH
num_z, den_z, dt = signal.cont2discrete(
    (num_s, den_s),
    Ts,
    method="zoh"
)

num_z = np.asarray(num_z).flatten()
den_z = np.asarray(den_z).flatten()

# Remover eventual coeficiente inicial nulo
num_z_sem_zeros = np.trim_zeros(num_z, trim="f")

# Sistema discreto H(z)
sistema_discreto = signal.dlti(
    num_z,
    den_z,
    dt=Ts
)

# Polos e zeros
polos_s = np.roots(den_s)
polos_z = np.roots(den_z)
zeros_z = np.roots(num_z_sem_zeros)

# Polos mapeados pela relação z = exp(sTs)
polos_mapeados = np.exp(polos_s * Ts)

# Verificação de estabilidade
estavel = np.all(np.abs(polos_z) < 1)

print("=== ANÁLISE NO PLANO-Z ===")
print(f"Frequência de amostragem: {fs:.0f} Hz")
print(f"Período de amostragem: {Ts:.6f} s")

print("\nFunção de transferência discreta:")
print("Numerador:", num_z)
print("Denominador:", den_z)

print("\nPolos contínuos:")
print(polos_s)

print("\nPolos discretos:")
print(polos_z)

print("\nPolos mapeados por z = exp(sTs):")
print(polos_mapeados)

print("\nZeros discretos:")
print(zeros_z)

print("\nMódulos dos polos discretos:")
print(np.abs(polos_z))

print("\nSistema discreto estável?", estavel)

# =====================================================
# RESPOSTAS TEMPORAIS
# =====================================================

duracao = 0.5

tempo = np.arange(0, duracao, Ts)

# Resposta contínua ao impulso
t_imp_c, y_imp_c = signal.impulse(
    sistema_continuo,
    T=tempo
)

# Resposta contínua ao degrau
t_step_c, y_step_c = signal.step(
    sistema_continuo,
    T=tempo
)

# Resposta discreta ao impulso
t_imp_d, y_imp_d = signal.dimpulse(
    sistema_discreto,
    n=len(tempo)
)

t_imp_d = np.asarray(t_imp_d)
y_imp_d = np.squeeze(y_imp_d)

# Escala para comparação aproximada com o impulso contínuo
y_imp_d_comparacao = y_imp_d / Ts

# Resposta discreta ao degrau
t_step_d, y_step_d = signal.dstep(
    sistema_discreto,
    n=len(tempo)
)

t_step_d = np.asarray(t_step_d)
y_step_d = np.squeeze(y_step_d)

# =====================================================
# FIGURA 1 - RESPOSTAS AO IMPULSO
# =====================================================

plt.figure(figsize=(11, 6))

plt.plot(
    t_imp_c,
    y_imp_c,
    label="Sistema contínuo",
    linewidth=2
)

plt.plot(
    t_imp_d,
    y_imp_d_comparacao,
    "o",
    markersize=3,
    label="Sistema discreto (escala ajustada)"
)

plt.title("Comparação das respostas ao impulso")
plt.xlabel("Tempo (s)")
plt.ylabel("Resposta")
plt.grid(True)
plt.legend()
plt.tight_layout()

# =====================================================
# FIGURA 2 - RESPOSTAS AO DEGRAU
# =====================================================

plt.figure(figsize=(11, 6))

plt.plot(
    t_step_c,
    y_step_c,
    label="Sistema contínuo",
    linewidth=2
)

plt.plot(
    t_step_d,
    y_step_d,
    "o",
    markersize=3,
    label="Sistema discreto"
)

plt.title("Comparação das respostas ao degrau")
plt.xlabel("Tempo (s)")
plt.ylabel("Deslocamento (m)")
plt.grid(True)
plt.legend()
plt.tight_layout()

# =====================================================
# FIGURA 3 - POLOS E ZEROS NO PLANO-Z
# =====================================================

fig, ax = plt.subplots(figsize=(9, 8))

theta = np.linspace(0, 2 * np.pi, 500)

ax.plot(
    np.cos(theta),
    np.sin(theta),
    "k--",
    label="Circunferência unitária"
)

ax.axhline(0, color="gray", linewidth=1)
ax.axvline(0, color="gray", linewidth=1)

ax.scatter(
    polos_z.real,
    polos_z.imag,
    marker="x",
    color="red",
    s=130,
    linewidths=2.5,
    label="Polos discretos"
)

ax.scatter(
    zeros_z.real,
    zeros_z.imag,
    facecolors="none",
    edgecolors="blue",
    s=130,
    linewidths=2,
    label="Zeros discretos"
)

ax.set_title("Polos e zeros do sistema no plano-z")
ax.set_xlabel("Parte real")
ax.set_ylabel("Parte imaginária")
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.grid(True)
ax.legend(loc="upper left")

plt.tight_layout()

# =====================================================
# FIGURA 4 - RESPOSTA EM FREQUÊNCIA
# =====================================================

frequencias_hz = np.linspace(0.1, 200, 3000)

omega_continua = 2 * np.pi * frequencias_hz
omega_discreta = 2 * np.pi * frequencias_hz / fs

# Resposta contínua
_, H_continua = signal.freqresp(
    sistema_continuo,
    w=omega_continua
)

# Resposta discreta
_, H_discreta = signal.freqz(
    num_z,
    den_z,
    worN=omega_discreta
)

plt.figure(figsize=(11, 6))

plt.plot(
    frequencias_hz,
    np.abs(H_continua),
    label="Sistema contínuo",
    linewidth=2
)

plt.plot(
    frequencias_hz,
    np.abs(H_discreta),
    "--",
    label="Sistema discreto",
    linewidth=2
)

plt.title("Comparação das respostas em frequência")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude (m/N)")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()
