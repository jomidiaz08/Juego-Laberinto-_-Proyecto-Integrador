import readchar 
import os
import random

class Juego:
    def __init__(self, carpeta_mapas):
        self.carpeta_mapas = carpeta_mapas
        self.inicializador_laberinto()

    def inicializador_laberinto(self):
        self.mapa = self.mapas_aleatorios()
        self.matriz_maze = self.cadena_a_matriz(self.mapa)
        self.posicion_inicio, self.posicion_fin = self.encontrar_posiciones_inicio_y_fin(self.matriz_maze)
        self.px, self.py = self.posicion_inicio
        self.principal()

    def mapas_aleatorios (self):
        mapa_archivos = os.listdir(self.carpeta_mapas)
        archivo = random.choice(mapa_archivos)
        carpeta_completo = os.path.join(self.carpeta_mapas, archivo)
        with open(carpeta_completo,'r', encoding='utf-8') as mapa_archivo:
            return mapa_archivo.read().strip()

    def cadena_a_matriz(self, cadena_maze):
        filas_maze = cadena_maze.strip().split("\n")
        matriz_maze = [list(fila) for fila in filas_maze]
        return matriz_maze

    def encontrar_posiciones_inicio_y_fin(self, matriz_maze):
        for i in range(len(matriz_maze)):
            for j in range(len(matriz_maze[i])):
                if matriz_maze[i][j] == "P":
                    posicion_inicio = (i, j)
                elif matriz_maze[i][j] == ".":
                    posicion_fin = (i, j)
        return posicion_inicio, posicion_fin

    def principal(self):
        while (self.px, self.py) != self.posicion_fin:
            self.terminal()
            self.mostrar_maze()

            tecla = readchar.readkey()
            if tecla == readchar.key.UP:
                nueva_px, nueva_py = self.px - 1, self.py
            elif tecla == readchar.key.DOWN:
                nueva_px, nueva_py = self.px + 1, self.py
            elif tecla == readchar.key.LEFT:
                nueva_px, nueva_py = self.px, self.py - 1
            elif tecla == readchar.key.RIGHT:
                nueva_px, nueva_py = self.px, self.py + 1
            else:
                continue

            if self.es_movimiento_valido(nueva_px, nueva_py):
                self.actualizar_posicion(nueva_px, nueva_py)

        self.terminal()
        self.mostrar_maze()
    
    def terminal(self):
        os.system("cls" if os.name == "nt" else "clear")

    def mostrar_maze(self):
        for fila in self.matriz_maze:
            print("".join(fila))

    def es_movimiento_valido(self, nueva_px, nueva_py):
        return (
            0 <= nueva_px < len(self.matriz_maze)
            and 0 <= nueva_py < len(self.matriz_maze[0])
            and self.matriz_maze[nueva_px][nueva_py] != "#"
        )

    def actualizar_posicion(self, nueva_px, nueva_py):
        self.matriz_maze[self.px][self.py] = "."
        self.px, self.py = nueva_px, nueva_py
        self.matriz_maze[self.px][self.py] = "P"
