import readchar
from readchar import key
def main():
    print("Presiona la tecla ↑. Para salir del bucle")

    while True:
        char = readchar.readkey()
        print(f"Tecla presionada: {char}")
        if char == key.UP:
            break

    print("Bucle finalizado.")

if __name__ == "__main__":
    main()