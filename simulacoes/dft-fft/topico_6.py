
import numpy as np
import matplotlib.pyplot as plt

# Frequências dos sinais (Hz)
frequencias = [50, 100, 200, 250]

# Frequências de amostragem (Hz)
frequencias_amostragem = [500, 1000]

# Conversões e apresentação dos resultados
print("CONVERSÃO DE FREQUÊNCIAS")
print("-" * 75)

for fs in frequencias_amostragem:

    print(f"\nFrequência de amostragem: {fs} Hz")
    print("Frequência | Ciclos/amostra | Radianos/amostra")

    for f in frequencias:

        # Frequência normalizada
        fn = f / fs

        # Frequência angular discreta
        omega = 2 * np.pi * fn

        print(
            f"{f:10.2f} | "
            f"{fn:14.4f} | "
            f"{omega:16.4f}"
        )

# Gráfico da frequência angular discreta
plt.figure(figsize=(10, 6))

for fs in frequencias_amostragem:

    # Valores de frequência do sinal
    f = np.linspace(0, fs / 2, 200)

    # Conversão para radianos por amostra
    omega = 2 * np.pi * f / fs

    plt.plot(
        f,
        omega,
        label=f"fs = {fs} Hz"
    )

plt.xlabel("Frequência do sinal (Hz)")
plt.ylabel("Frequência angular (rad/amostra)")
plt.title("Relação entre frequência física e frequência angular discreta")

plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Comparação de frequências normalizadas
plt.figure(figsize=(10, 6))

for fs in frequencias_amostragem:

    f = np.linspace(0, fs / 2, 200)

    fn = f / fs

    plt.plot(
        f,
        fn,
        label=f"fs = {fs} Hz"
    )

plt.xlabel("Frequência do sinal (Hz)")
plt.ylabel("Frequência normalizada (ciclos/amostra)")
plt.title("Frequência normalizada para diferentes amostragens")

plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
