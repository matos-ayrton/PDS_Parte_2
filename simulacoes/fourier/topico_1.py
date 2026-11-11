import numpy as np
import matplotlib.pyplot as plt

# Índices das amostras
n = np.arange(0, 64)

# --------------------------------------------------
# 1. Senoides com diferentes frequências
# --------------------------------------------------

frequencias = [0.05, 0.10, 0.20]

plt.figure(figsize=(10, 5))

for f in frequencias:
    x = np.cos(2 * np.pi * f * n)

    plt.plot(
        n, x,
        marker='o',
        markersize=3,
        label=f'f = {f} ciclos/amostra'
    )

plt.title('Senoides com diferentes frequências')
plt.xlabel('Índice da amostra (n)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 2. Modificação da fase
# --------------------------------------------------

omega = 2 * np.pi * 0.10
fases = [0, np.pi / 4, np.pi / 2]

plt.figure(figsize=(10, 5))

for fase in fases:
    x = np.cos(omega * n + fase)

    plt.plot(
        n, x,
        marker='o',
        markersize=3,
        label=f'Fase = {fase / np.pi:.2f}π rad'
    )

plt.title('Influência da fase na senoide')
plt.xlabel('Índice da amostra (n)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 3. Modificação da amplitude
# --------------------------------------------------

amplitudes = [1, 2, 3]
omega = 2 * np.pi * 0.10

plt.figure(figsize=(10, 5))

for A in amplitudes:
    x = A * np.cos(omega * n)

    plt.plot(
        n, x,
        marker='o',
        markersize=3,
        label=f'Amplitude = {A}'
    )

plt.title('Influência da amplitude na senoide')
plt.xlabel('Índice da amostra (n)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 4. Parte real e imaginária da exponencial complexa
# --------------------------------------------------

omega = np.pi / 8

z = np.exp(1j * omega * n)

parte_real = np.real(z)
parte_imaginaria = np.imag(z)

plt.figure(figsize=(10, 5))

plt.plot(
    n, parte_real,
    marker='o',
    markersize=3,
    label='Parte real: cos(ωn)'
)

plt.plot(
    n, parte_imaginaria,
    marker='s',
    markersize=3,
    label='Parte imaginária: sen(ωn)'
)

plt.title('Partes real e imaginária da exponencial complexa')
plt.xlabel('Índice da amostra (n)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()