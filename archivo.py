from juego import Juego
from functools import reduce

class Juegoarchivo(Juego):
    def __init__(self, carpeta_mapas):
        super().__init__(carpeta_mapas)

    def leer_mapa_archivo(self, nombre_archivo):
            with open(nombre_archivo, "r") as archivo_mapa:
                lineas = archivo_mapa.readlines()
            coordenadas = lineas[0].strip().split()
            filas_mapa = reduce(lambda x, y: x + y, lineas[1:])
            return coordenadas, filas_mapa.strip()