import numpy as np
import matplotlib.pyplot as plt


def simulate_trajectory(T, dt):
    # Generovanie náhodných parametrov
    A = np.random.uniform(0, 1)
    omega = np.random.uniform(0, 2 * np.pi)
    phi = np.random.uniform(0, 2 * np.pi)

    # Simulácia trajektórie
    t = np.arange(0, T, dt)
    X_t = A * np.sin(omega * t + phi)

    return X_t, t


def estimate_probability(T, dt, num_simulations):
    count_J = 0  # Počet trajektórií, kde nastal jav J

    for _ in range(num_simulations):
        X_t, t = simulate_trajectory(T, dt)
        if np.any(X_t > 0.5):  # Detekcia javu J
            count_J += 1

    # Odhad pravdepodobnosti
    probability_J = count_J / num_simulations
    return probability_J


# Parametre simulácie
T = 10  # Časový interval
dt = 0.01  # Časový krok
num_simulations = 10000  # Počet simulácií

# Odhad pravdepodobnosti
probability_J = estimate_probability(T, dt, num_simulations)
print(f"Pravdepodobnosť javu J: {probability_J}")

# Vizualizácia niekoľkých trajektórií
plt.figure(figsize=(10, 6))
for _ in range(5):
    X_t, t = simulate_trajectory(T, dt)
    plt.plot(t, X_t)
plt.axhline(y=0.5, color='r', linestyle='--', label='X_t = 0.5')
plt.xlabel('Čas (t)')
plt.ylabel('X_t')
plt.title('Náhodné trajektórie procesu X_t')
plt.legend()
plt.show()