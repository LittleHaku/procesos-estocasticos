import numpy as np
import matplotlib.pyplot as plt

def simulate_wiener_process(T, W0, M, N):
    """Simula un proceso de Wiener.

    Args:
        T (float): Tiempo final.
        W0 (float): Valor inicial.
        M (int): Número de simulaciones.
        N (int): Número de pasos.

    Returns:
        np.ndarray: Simulaciones del proceso de Wiener.
    """
    dT = T / N
    W = np.empty((M, N+1))
    W[:, 0] = W0
    W[:, 1:] = np.sqrt(dT) * np.random.randn(M, N)
    W = np.cumsum(W, axis=1)
    return W

def plot_time_simulations(W, t_values, process_name):
    """
    Grafica las simulaciones del proceso dado.

    Args:
        W (array): Simulaciones del proceso de Wiener.
        t_values (array): Valores de tiempo.
        process_name (str): Nombre del proceso.
    """

    mean_empirical = np.mean(W, axis=0)
    variance_empirical = np.var(W, axis=0)
    plt.figure(figsize=(10, 6))
    plt.plot(t_values, W.T, alpha=0.3)
    plt.plot(t_values, mean_empirical, color="black", linewidth=2, label="Media Empírica")
    plt.plot(t_values, mean_empirical + np.sqrt(variance_empirical), color="green", label="Desviación Estándar (1 sigma) 68.3%", linestyle="--")
    plt.plot(t_values, mean_empirical - np.sqrt(variance_empirical), color="green", linestyle="--")
    plt.plot(t_values, mean_empirical + 2 * np.sqrt(variance_empirical), color="orange", label="Desviación Estándar (2 sigma) 95.4%", linestyle="--")
    plt.plot(t_values, mean_empirical - 2 * np.sqrt(variance_empirical), color="orange", linestyle="--")
    plt.plot(t_values, mean_empirical + 3 * np.sqrt(variance_empirical), color="red", label="Desviación Estándar (3 sigma) 99.7%", linestyle="--")
    plt.plot(t_values, mean_empirical - 3 * np.sqrt(variance_empirical), color="red", linestyle="--")
    plt.xlabel("tiempo (s)")
    plt.ylabel("W(t)")
    plt.title(f"Simulaciones del proceso {process_name}")
    plt.legend()
    plt.grid()
    plt.show()


def estimate_autocovariance(W, t_values, fixed_s):
    """
    Estima la autocovarianza γ(t, fixed_s).

    Args:
        W (array): Simulaciones del proceso de Wiener.
        t_values (array): Valores de tiempo.
        fixed_s (float): Valor fijo de s.

    Returns:
        np.ndarray: Autocovarianza empírica.
    """
    W_s = W[:, np.argmin(np.abs(t_values - fixed_s))]
    return np.mean(W * W_s[:, np.newaxis], axis=0)

def simulate_modified_processes(T, M, N, rho=0.8, c=2.0):
    """Simula procesos con covarianzas similares al proceso de Wiener.

    Args:
        T (float): Tiempo final.
        M (int): Número de simulaciones.
        N (int): Número de pasos.
        rho (float): Correlación para el primer proceso.
        c (float): Constante de escalado para el tercer proceso.

    Returns:
        tuple: Simulaciones de los procesos Y1, Y2, Y3.
    """
    W1 = simulate_wiener_process(T, 0, M, N)
    W2 = simulate_wiener_process(T, 0, M, N)

    # Proceso 1
    Y1 = rho * W1 + np.sqrt(1 - rho**2) * W2

    # Proceso 2
    Y2 = -W1

    # Proceso 3
    Y3 = np.sqrt(c) * simulate_wiener_process(T, 0, M, N // int(c))

    return Y1, Y2, Y3
