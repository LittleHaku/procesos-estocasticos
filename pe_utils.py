import numpy as np

def simulate_markov_chain(P, initial_state, N, seed=False):
    """Simula una cadena de Markov con matriz de transición P, estado inicial initial_state y longitud N.
    Devuelve un array con los estados de la cadena de Markov.

    Args:
        P (np.array): Matriz de transición de la cadena de Markov.
        initial_state (int): Estado inicial de la cadena de Markov (índice basado en 0).
        N (int): Longitud de la cadena de Markov.
        seed (bool, optional): Si se quiere fijar semilla o no. Defaults to False.

    Returns:
        np.array: Array con los estados de la cadena de Markov.
    """

    # Fijamos la semilla si es necesario
    if seed:
        np.random.seed(42)

    # Preasignar el array para almacenar los estados
    states = np.zeros(N + 1, dtype=int)
    states[0] = initial_state  # Establecer el estado inicial

    for i in range(N):
        current_state = states[i] - 1  # Estado actual
        # Elegir el próximo estado basado en las probabilidades
        next_state = np.random.choice(len(P), p=P[current_state])
        states[i + 1] = next_state + 1  # Guardar el próximo estado +1 porque empiezan en uno en el enunciado

    return states
