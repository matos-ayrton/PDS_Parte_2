
import numpy as np
import matplotlib.pyplot as plt

# Definição da sequência impulso unitário
n = np.arange(-10, 11)
x = np.zeros(len(n))
x[n == 0] = 1

# Valores de frequência angular
omega = np.linspace(-np.pi, np.pi, 1000)

# Cálculo numérico da DTFT
X = np.sum(
    x[:, np.newaxis] *
    np.exp(-1j * np.outer(n, omega)),
    axis=0
)

# Espectro de magnitude e fase
magnitude = np.abs(X)
fase = np.angle(X)

# Gráfico do sinal no domínio do tempo
plt.figure(figsize=(10, 4))
plt.stem(n, x)
plt.title('Impulso unitário no domínio do tempo')
plt.xlabel('Índice da amostra (n)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico do espectro de magnitude
plt.figure(figsize=(10, 4))
plt.plot(omega, magnitude)
plt.title('Espectro de magnitude da DTFT')
plt.xlabel('Frequência angular (rad/amostra)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico do espectro de fase
plt.figure(figsize=(10, 4))
plt.plot(omega, fase)
plt.title('Espectro de fase da DTFT')
plt.xlabel('Frequência angular (rad/amostra)')
plt.ylabel('Fase (rad)')
plt.grid(True)
plt.tight_layout()
plt.show()