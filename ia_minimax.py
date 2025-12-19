from typing import List
from collections import deque
from config import Grid, Pos, State
from tablero import neighbors

def terminal(state: State) -> bool:
    gato, raton = state
    return gato == raton

# BFS (Busqueda en amplitud)para encontrar la distancia más corta.
def shortest_path_length(grid: Grid, start: Pos, goal: Pos) -> int:
    if start == goal:
        return 0
    visitados: dict[Pos, int] = {start: 0}
    cola: deque[Pos] = deque([start])
    while cola:
        actual = cola.popleft()
        dist_actual = visitados[actual]
        for vecino in neighbors(grid, actual):
            if vecino not in visitados:
                visitados[vecino] = dist_actual + 1
                if vecino == goal:
                    return visitados[vecino]
                cola.append(vecino)
    # No hay camino
    return 999

def evaluate(grid: Grid, state: State) -> int:
    gato, raton = state

    if gato == raton:   
        return 10_000  # victoria del gato

    dist = shortest_path_length(grid, gato, raton)

    if dist == 999:
        # No hay forma de alcanzar al ratón
        return -10_000

    return 1_000 - dist

def moves_for_cat(grid: Grid, state: State) -> List[State]:
    gato, raton = state
    siguientes: List[State] = []
    for nueva_pos_gato in neighbors(grid, gato):
        siguientes.append((nueva_pos_gato, raton))
    # Si por algún motivo no hubiera vecinos libres, se queda quieto
    return siguientes or [state]


def moves_for_mouse(grid: Grid, state: State) -> List[State]:
    gato, raton = state
    siguientes: List[State] = []
    for nueva_pos_raton in neighbors(grid, raton):
        siguientes.append((gato, nueva_pos_raton))
    # Si no hay movimientos posibles, se queda en el lugar
    return siguientes or [state]

def minimax(grid: Grid,state: State,depth: int,is_max_turn: bool,alpha: int,beta: int,) -> int:

    if terminal(state) or depth == 0:
        val = evaluate(grid, state)
        return val

    if is_max_turn:
        mejor_valor = -10**9

        for estado_hijo in moves_for_cat(grid, state):
            valor_hijo = minimax(grid, estado_hijo, depth - 1, False, alpha, beta)
            mejor_valor = max(mejor_valor, valor_hijo)
            alpha = max(alpha, mejor_valor)

            # Poda: MIN no permitirá llegar aquí si ya tiene algo mejor
            if beta <= alpha:
                break

        return mejor_valor

    # Turno del RATÓN (MIN)
    else:
        mejor_valor = 10**9

        for estado_hijo in moves_for_mouse(grid, state):
            valor_hijo = minimax(grid, estado_hijo, depth - 1, True, alpha, beta)
            mejor_valor = min(mejor_valor, valor_hijo)
            beta = min(beta, mejor_valor)

            # Poda: MAX no permitirá llegar aquí si ya tiene algo mejor
            if beta <= alpha:
                break

        return mejor_valor

def best_move_for_cat(grid: Grid, state: State, depth: int) -> State:
 
    mejor_valor = -10**9
    mejor_estado = state

    for child in moves_for_cat(grid, state):
        valor_hijo = minimax(grid, child, depth - 1, False, -10**9, 10**9)
        if valor_hijo > mejor_valor:
            mejor_valor = valor_hijo
            mejor_estado = child

    return mejor_estado

def best_move_for_mouse(grid: Grid, state: State, depth: int) -> State:

    mejor_valor = 10**9
    mejor_estado = state

    for child in moves_for_mouse(grid, state):
        valor_hijo = minimax(grid, child, depth - 1, True, -10**9, 10**9)
        if valor_hijo < mejor_valor:
            mejor_valor = valor_hijo
            mejor_estado = child

    return mejor_estado