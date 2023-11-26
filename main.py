import readchar
import os
from readchar import key

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
    print("\n" * 100)

def cadena_a_matriz(cadena_maze):
    filas_maze = cadena_maze.strip().split("\n")
    matriz_maze = [list(fila) for fila in filas_maze]
    return matriz_maze

def encontrar_posiciones_inicio_y_fin(matriz_maze):
    for i in range(len(matriz_maze)):
        for j in range(len(matriz_maze[i])):
            if matriz_maze[i][j] == "P":
                posicion_inicio = (i, j)
            elif matriz_maze[i][j] == ".":
                posicion_fin = (i, j)
    return posicion_inicio, posicion_fin

def principal(mapa):
    matriz_maze = cadena_a_matriz(mapa)
    posicion_inicio, posicion_fin = encontrar_posiciones_inicio_y_fin(matriz_maze)
    px, py = posicion_inicio

    while (px, py) != posicion_fin:
        limpiar()
        for fila in matriz_maze:
            print("".join(fila))

        tecla = readchar.readkey()
        if tecla == key.UP:
            nueva_px, nueva_py = px - 1, py
        elif tecla == key.DOWN:
            nueva_px, nueva_py = px + 1, py
        elif tecla == key.LEFT:
            nueva_px, nueva_py = px, py - 1
        elif tecla == key.RIGHT:
            nueva_px, nueva_py = px, py + 1
        else:
            continue
        if (
            0 <= nueva_px < len(matriz_maze)
            and 0 <= nueva_py < len(matriz_maze[0])
            and matriz_maze[nueva_px][nueva_py] != "#"
        ):
            matriz_maze[px][py] = "."
            px, py = nueva_px, nueva_py
            matriz_maze[px][py] = "P"

    clear_terminal()  

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    limpiar()
    presentacion = input("ingresa tu nombre: ")
    print("Bienvenido, este es mi juego {}".format(presentacion))

    limpiar()
    mapa = """
##########
#P.......#
#.##..####
#...#.#..#
###.#.###.
#.....#..#
#.###.#..#
#...#....#
########.#
"""
    principal(mapa)