import readchar 
import os
def clear_terminal():

    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    numero = 0

    while numero <= 50:
    
        clear_terminal()

        print(f"Número: {numero}")

        key = readchar.readkey()

        if key == 'n':
            numero += 1

if __name__ == "__main__":
    main()