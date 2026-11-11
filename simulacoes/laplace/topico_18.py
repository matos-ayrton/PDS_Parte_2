import numpy as np
import matplotlib.pyplot as plt

# Polos no plano-s
polos_s = [
    -1,
    -2,
    -5,
    0,
    1,
    -1 + 4j,
    -1 - 4j,
    0.5 + 3j,
    0.5 - 3j
]

# Períodos de amostragem
periodos = [0.05, 0.1, 0.2]

# Configuração das figuras
fig, eixos = plt.subplots(1, 2, figsize=(14, 6))

# Plano-s
ax_s = eixos[0]

for polo in polos_s:
    ax_s.scatter(
        np.real(polo),
        np.imag(polo),
        marker="x",
        s=80
    )

ax_s.axhline(0, color="black", linewidth=0.8)
ax_s.axvline(0, color="black", linewidth=0.8)

ax_s.set_title("Polos no plano-s")
ax_s.set_xlabel("Parte real")
ax_s.set_ylabel("Parte imaginária")
ax_s.grid(True)
ax_s.set_aspect("equal", adjustable="datalim")

# Plano-z
ax_z = eixos[1]

# Círculo unitário
angulo = np.linspace(0, 2*np.pi, 500)

ax_z.plot(
    np.cos(angulo),
    np.sin(angulo),
    linestyle="--",
    color="black",
    label="Círculo unitário"
)

# Mapeamento para diferentes períodos
for Ts in periodos:

    polos_z = [
        np.exp(polo * Ts)
        for polo in polos_s
    ]

    ax_z.scatter(
        np.real(polos_z),
        np.imag(polos_z),
        label=f"Ts = {Ts} s"
    )

ax_z.axhline(0, color="black", linewidth=0.8)
ax_z.axvline(0, color="black", linewidth=0.8)

ax_z.set_title("Polos transformados no plano-z")
ax_z.set_xlabel("Parte real")
ax_z.set_ylabel("Parte imaginária")
ax_z.grid(True)
ax_z.set_aspect("equal", adjustable="datalim")
ax_z.legend()

plt.tight_layout()
plt.show()

# Apresentação dos valores calculados
print("Mapeamento dos polos do plano-s para o plano-z")

for Ts in periodos:

    print(f"\nPeríodo de amostragem: {Ts} s")

    for polo in polos_s:

        polo_z = np.exp(polo * Ts)

        print(
            f"s = {polo:>12} "
            f"-> z = {polo_z.real:.4f} "
            f"+ j({polo_z.imag:.4f}) "
            f"| módulo = {abs(polo_z):.4f}"
        )