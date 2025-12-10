
from typing import List, Tuple

# Tipos
Grid = List[List[str]]
Pos = Tuple[int, int]
State = Tuple[Pos, Pos]  # (gato, raton)

# Tablero base: # = pared, . = libre, G = gato, R = ratón
RAW_MAP = [
    "#################",
    "#R......#.......#",
    "#.#####.#.#####.#",
    "#.....#.#.#.....#",
    "#####.#.#.#.#####",
    "#.....#...#.....#",
    "#.#####.#.#####.#",
    "#.#.....#.....#.#",
    "#.#.#########.#.#",
    "#.#.....#.....#.#",
    "#.#####.#.#####.#",
    "#.....#.#.#.....#",
    "#####.#.#.#.#####",
    "#.....#...#.....#",
    "#.#####.#.#####.#",
    "#.......#......G#",
    "#################",
]

# Parámetros del juego
DEPTH = 4          # Profundidad de búsqueda de Minimax
MAX_TURNS = 60     # Máximo de turnos del juego