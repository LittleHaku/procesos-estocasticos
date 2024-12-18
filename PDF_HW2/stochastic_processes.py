import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.animation as animation

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
    Grafica las primeras 50 simulaciones del proceso dado (para poder visualizar mejor).
    También grafica la media empírica y las desviaciones estándar (1, 2 y 3 sigmas).

    Args:
        W (array): Simulaciones del proceso de Wiener.
        t_values (array): Valores de tiempo.
        process_name (str): Nombre del proceso.
    """

    W_subset = W[:50]
    mean_empirical = np.mean(W, axis=0)
    variance_empirical = np.var(W, axis=0)
    plt.figure(figsize=(10, 6))
    plt.plot(t_values, W_subset.T, alpha=0.3)
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

def plot_final_distribution(W, process_name):
    """
    Grafica un histograma con la distribucion final del proceso teórica y empírica.

    Args:
        W (array): Simulaciones del proceso.
        process_name (str): Nombre del proceso.
    """
    final_values = W[:, -1]
    x = np.linspace(np.min(final_values), np.max(final_values), 100)
    theoretical_density = norm.pdf(x, loc=0, scale=1)

    plt.figure(figsize=(10, 6))
    plt.hist(final_values, bins=30, density=True, alpha=0.6, label="Histograma Empírico")
    plt.plot(x, theoretical_density, label="Densidad Teórica N(0,1)", linewidth=2, color="red")
    plt.xlabel("Valor Final")
    plt.ylabel("Densidad")
    plt.title(f"Distribución Final del Proceso {process_name}")
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


def animate_simulation_distribution(W, x0, t0, T, num_frames):
    """
    Crea una animación de la evolución de la distribución de un proceso.

    Args:
        W (numpy.ndarray): Simulaciones del proceso de Wiener.
        x0 (float): Valor inicial B(t0).
        t0 (float): Tiempo inicial.
        T (float): Duración del intervalo de simulación.
        num_frames (int): Número de cuadros en la animación.
    """
    t_grid = np.linspace(t0, t0 + T, num_frames)
    N = W.shape[1] - 1
    indices = np.linspace(0, N, num_frames, dtype=int)

    fig, ax = plt.subplots()
    bins = 30
    # Inicializar el histograma
    _ = ax.hist(W[:, 0], bins=bins, density=True, alpha=0.6, color='g', label='Histograma Empírico')
    x = np.linspace(np.min(W), np.max(W), 1000)
    pdf = norm.pdf(x, loc=x0, scale=np.sqrt(t_grid[0] - t0))
    _,  = ax.plot(x, pdf, 'r-', lw=2, label='Densidad Teórica')
    ax.set_xlabel('B(t)')
    ax.set_ylabel('Densidad')
    ax.set_title(f'Evolución de la Distribución de B(t) en t={t_grid[0]:.2f}')
    ax.legend()
    ax.grid(True)

    def update(frame):
        ax.cla()
        current_t = t_grid[frame]
        current_data = W[:, indices[frame]]
        ax.hist(current_data, bins=bins, density=True, alpha=0.6, color='g', label='Histograma Empírico')
        pdf = norm.pdf(x, loc=x0, scale=np.sqrt(current_t - t0))
        ax.plot(x, pdf, 'r-', lw=2, label='Densidad Teórica')
        ax.set_xlabel('B(t)')
        ax.set_ylabel('Densidad')
        ax.set_title(f'Evolución de la Distribución de B(t) en t={current_t:.2f}')
        ax.legend()
        ax.grid(True)

    ani = animation.FuncAnimation(fig, update, frames=num_frames, repeat=False)
    plt.close(fig)
    return ani

def simulate_brownian_bridge(T, M, N):
    """
    Simula un puente browniano.

    Args:
        T (float): Tiempo final.
        M (int): Número de simulaciones.
        N (int): Número de pasos.

    Returns:
        np.ndarray: Simulaciones del puente browniano.
    """
    W = simulate_wiener_process(T, 0, M, N)
    t_values = np.linspace(0, T, N + 1)
    W_T = W[:, -1]
    BB = W - np.outer(W_T, t_values / T)
    return BB
