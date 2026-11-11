
import numpy as np
import matplotlib.pyplot as plt

# Intervalo de tempo
t = np.linspace(0, 5, 1000)

# Geração dos sinais
x_decrescente = np.exp(-2 * t)
x_crescente = np.exp(t)
x_senoidal = np.sin(3 * t)

# Criação da figura
fig, eixos = plt.subplots(2, 2, figsize=(13, 9))

# 1. Exponencial decrescente
eixos[0, 0].plot(t, x_decrescente)
eixos[0, 0].set_title("Exponencial decrescente: e^(-2t)")
eixos[0, 0].set_xlabel("Tempo (s)")
eixos[0, 0].set_ylabel("Amplitude")
eixos[0, 0].grid(True)

# 2. Exponencial crescente
eixos[0, 1].plot(t, x_crescente)
eixos[0, 1].set_title("Exponencial crescente: e^t")
eixos[0, 1].set_xlabel("Tempo (s)")
eixos[0, 1].set_ylabel("Amplitude")
eixos[0, 1].grid(True)

# 3. Senoide
eixos[1, 0].plot(t, x_senoidal)
eixos[1, 0].set_title("Sinal senoidal: sin(3t)")
eixos[1, 0].set_xlabel("Tempo (s)")
eixos[1, 0].set_ylabel("Amplitude")
eixos[1, 0].grid(True)

# 4. Representação no plano-s
ax = eixos[1, 1]

# Posições das componentes no plano-s
ax.scatter(-2, 0, label="s = -2")
ax.scatter(1, 0, label="s = 1")
ax.scatter(0, 3, label="s = j3")
ax.scatter(0, -3, label="s = -j3")

ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)

ax.set_title("Representação no plano-s")
ax.set_xlabel("Parte real (σ)")
ax.set_ylabel("Parte imaginária (ω)")
ax.grid(True)
ax.legend()
ax.set_xlim(-3, 2)
ax.set_ylim(-4, 4)

plt.tight_layout()
plt.show()
