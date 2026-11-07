"""Punto de entrada del juego del ahorcado."""
from utils import get_valid_letter


def main():
    """Pide letras al jugador (prueba temporal de la tarea 3)."""
    guessed_letters = []
    try:
        while True:
            letter = get_valid_letter(guessed_letters)
            guessed_letters.append(letter)
            print(f"Letra aceptada: {letter}")
    except KeyboardInterrupt:
        print("\nJuego terminado.")


if __name__ == "__main__":
    main()
