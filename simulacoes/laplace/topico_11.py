
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Tempo utilizado nas simulacoes
t = np.linspace(0, 8, 1500)

fig, eixos = plt.subplots(2, 2, figsize=(13, 9))

# -------------------------------------------------
# 1. Sistema de primeira ordem - variacao de tau
# -------------------------------------------------

ax = eixos[0, 0]

K = 1
valores_tau = [0.2, 0.5, 1.0]

for tau in valores_tau:
    num = [K]
    den = [tau, 1]

    sistema = signal.TransferFunction(num, den)
    tempo, resposta = signal.step(sistema, T=t)

    ax.plot(tempo, resposta, label=f'tau = {tau}')

ax.set_title('Variacao da constante de tempo')
ax.set_xlabel('Tempo (s)')
ax.set_ylabel('Amplitude')
ax.grid(True)
ax.legend()

# -------------------------------------------------
# 2. Sistema de primeira ordem - variacao de K
# -------------------------------------------------

ax = eixos[0, 1]

tau = 0.5
valores_K = [0.5, 1.0, 2.0]

for K in valores_K:
    num = [K]
    den = [tau, 1]

    sistema = signal.TransferFunction(num, den)
    tempo, resposta = signal.step(sistema, T=t)

    ax.plot(tempo, resposta, label=f'K = {K}')

ax.set_title('Variacao do ganho')
ax.set_xlabel('Tempo (s)')
ax.set_ylabel('Amplitude')
ax.grid(True)
ax.legend()

# -------------------------------------------------
# 3. Sistema de segunda ordem - variacao de zeta
# -------------------------------------------------

ax = eixos[1, 0]

wn = 4
K = 1
valores_zeta = [0.2, 0.7, 1.0, 1.5]

for zeta in valores_zeta:
    num = [K * wn**2]
    den = [1, 2*zeta*wn, wn**2]

    sistema = signal.TransferFunction(num, den)
    tempo, resposta = signal.step(sistema, T=t)

    ax.plot(tempo, resposta, label=f'zeta = {zeta}')

ax.set_title('Variacao do fator de amortecimento')
ax.set_xlabel('Tempo (s)')
ax.set_ylabel('Amplitude')
ax.grid(True)
ax.legend()

# -------------------------------------------------
# 4. Sistema de segunda ordem - variacao de wn
# -------------------------------------------------

ax = eixos[1, 1]

zeta = 0.5
valores_wn = [2, 4, 8]

for wn in valores_wn:
    num = [K * wn**2]
    den = [1, 2*zeta*wn, wn**2]

    sistema = signal.TransferFunction(num, den)
    tempo, resposta = signal.step(sistema, T=t)

    ax.plot(tempo, resposta, label=f'wn = {wn}')

ax.set_title('Variacao da frequencia natural')
ax.set_xlabel('Tempo (s)')
ax.set_ylabel('Amplitude')
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.show()
