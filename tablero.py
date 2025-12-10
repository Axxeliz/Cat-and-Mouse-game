from typing import List, Tuple
from config import Grid, Pos, State

def to_grid(raw: List[str]) -> Grid:
    return [list(row) for row in raw]

def find_pos(grid: Grid, ch: str) -> Pos:
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == ch:
                return (r, c)
    raise ValueError(f"No se encontró {ch} en el mapa.")

def is_free(grid: Grid, pos: Pos) -> bool:
    r, c = pos
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != "#"

def neighbors(grid: Grid, pos: Pos) -> List[Pos]:
    r, c = pos
    candidates = [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]
    return [p for p in candidates if is_free(grid, p)]

def draw(grid: Grid, gato: Pos, raton: Pos) -> None:  # Dibuja una copia temporal con G y R
    
    tmp = [row[:] for row in grid]
    gr, gc = gato
    rr, rc = raton
    tmp[gr][gc] = "G"
    tmp[rr][rc] = "R"
    for row in tmp:
        print("".join(row))
    print()