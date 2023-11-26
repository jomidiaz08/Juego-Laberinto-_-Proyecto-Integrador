from archivo import Juegoarchivo

def main():
    carpeta_mapas = "carpeta_de_mapas/"
    presentacion = input("ingresa tu nombre: ")
    print("Bienvenido, este es mi juego {}".format(presentacion))
    juego = Juegoarchivo(carpeta_mapas)
    juego.principal()

if __name__ == "__main__":
    main()
