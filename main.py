"""Punto de entrada del juego del ahorcado."""
from game import HangmanGame
from utils import get_random_word, get_valid_letter


def main():
    """Pide letras al jugador y muestra si acertó (prueba temporal)."""
    game = HangmanGame(get_random_word())
    try:
        while True:
            letter = get_valid_letter(game.guessed_letters)
            if game.process_guess(letter):
                print("¡Bien!")
            else:
                print("Fallaste")
    except KeyboardInterrupt:
        print("\nJuego terminado.")


if __name__ == "__main__":
    main()
