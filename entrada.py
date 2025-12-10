from config import Grid, State
from tablero import is_free

KEY2DIR = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1),}

def apply_mouse_input(grid: Grid, state: State, key: str) -> State:
    gato, raton = state
    dr, dc = KEY2DIR.get(key.lower(), (0, 0))
    new_pos = (raton[0] + dr, raton[1] + dc)
    if is_free(grid, new_pos):
        return (gato, new_pos)
    return state  # movimiento inválido -> se queda
def apply_cat_input(grid: Grid, state: State, key: str) -> State:
    gato, raton = state
    dr, dc = KEY2DIR.get(key.lower(), (0, 0))
    new_pos = (gato[0] + dr, gato[1] + dc)
    if is_free(grid, new_pos):
        return (new_pos, raton)
    return state  # movimiento inválido -> se queda