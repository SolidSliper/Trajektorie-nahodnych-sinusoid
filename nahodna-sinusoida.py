import numpy as np
import matplotlib.pyplot as plt

def simulate_trajectory(T, dt):
    # Generovanie náhodných parametrov
    A = np.random.uniform(0, 1)
    omega = np.random.uniform(0, 2 * np.pi)
    phi = np.random.uniform(0, 2 * np.pi)

    # Simulácia trajektórie na [0, π]
    t = np.arange(0, T, dt)
    X_t = A * np.sin(omega * t + phi)
    return X_t, t

def estimate_probability(num_samples=100000, c=0.5):
    count = 0
    for _ in range(num_samples):
        omega = np.random.uniform(0, 2 * np.pi)
        phi = np.random.uniform(0, 2 * np.pi)
        t_values = np.linspace(0, np.pi, 100)
        if np.any(np.sin(omega * t_values + phi) > c):
            count += 1
    return count / num_samples

# Parametre simulácie
T = np.pi
dt = 0.01
num_simulations = 10000

# Odhad pravdepodobnosti
probability_J = estimate_probability(num_simulations, c=0.5)
print(f"Monte Carlo simulation estimate: {probability_J}")

# Vizualizácia trajektórií
plt.figure(figsize=(10, 6))
for _ in range(5):
    X_t, t = simulate_trajectory(T, dt)
    plt.plot(t, X_t, alpha=0.7)
plt.axhline(y=0.5, color='r', linestyle='--', label='Threshold 0.5')
plt.xlabel('Time (t)')
plt.ylabel('X_t')
plt.title('Random Trajectories on [0, π]')
plt.xlim(0, np.pi)  # Explicitné ohraničenie osi x
plt.legend()
plt.show()
