from config import RAW_MAP, DEPTH, MAX_TURNS, State
from tablero import to_grid, find_pos, draw
from ia_minimax import terminal, best_move_for_cat, best_move_for_mouse
from entrada import apply_mouse_input, apply_cat_input
import os

def main():
    #  Elegir dificultad
    global DEPTH
    try:
        nuevo = int(input("Elige dificultad (DEPTH): "))
        DEPTH = nuevo
    except:
        print("Dificultad inválida. Usando dificultad estandar.")

    print("Dificultad actual =", DEPTH)

    # cargar el tablero
    grid = to_grid(RAW_MAP)
    gato = find_pos(grid, "G")
    raton = find_pos(grid, "R")

    # Limpiar símbolos del mapa base
    gr, gc = gato
    rr, rc = raton
    grid[gr][gc] = "."
    grid[rr][rc] = "."

    state: State = (gato, raton)

    # Elegir rol del jugador 
    os.system("cls")
    print("¿Quién quieres ser?")
    print("1. RATÓN, huir del gato")
    print("2. GATO, perseguir al ratón")
    player = input("> ").strip()

    if player == "2":
        # Jugador controla al GATO (MAX)
        player_is_mouse = False
        print("\nHas elegido controlar al GATO (G)\n")
    else:
        # Jugador controla al RATÓN (MIN)
        player_is_mouse = True
        print("\nHas elegido controlar al RATÓN (R)\n")

    print("Controles: w/a/s/d para mover | q para salir.\n")

    # Bucle del juego
    turn = 0
    while turn < MAX_TURNS and not terminal(state):
        print(f"Turno #{turn}")
        os.system("cls")
        draw(grid, *state)
        # TURNO DEL JUGADOR
        key = input("Tu movimiento: ").strip().lower()
        if key == "q":
            print("Saliendo...")
            return

        if player_is_mouse:  
            # Jugador mueve al RATÓN (MIN)
            state = apply_mouse_input(grid, state, key)
        else:
            # Jugador mueve al GATO (MAX)
            state = apply_cat_input(grid, state, key)

        if terminal(state):
            break

        # TURNO DE LA IA
        if player_is_mouse:
            # Jugador = ratón → IA controla al GATO (MAX)
            state = best_move_for_cat(grid, state, DEPTH)
        else:
            # Jugador = gato → IA controla al RATÓN (MIN)
            state = best_move_for_mouse(grid, state, DEPTH)
        turn += 1

    # Final del juego
    os.system("cls")
    draw(grid, *state)

    gato_pos, raton_pos = state

    if gato_pos == raton_pos:
        print("¡El GATO atrapó al RATÓN!")
    else:
        print("Fin de turnos. El RATÓN sobrevivió.")

if __name__ == "__main__":
    main()