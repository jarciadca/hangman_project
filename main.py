"""
Punto de entrada del juego del ahorcado.

Autor: Cristian
Curso: Desarrollo de Software con IA
"""
from utils import get_random_word, get_valid_letter, display_status
from game import HangmanGame


def main():
    """Bucle principal del juego con condiciones de fin."""
    palabra = get_random_word()
    juego = HangmanGame(palabra)

    # Se ejecuta MIENTRAS no gane Y no pierda
    while not juego.is_won() and not juego.is_lost():
        display_status(juego)
        letra = get_valid_letter(juego.guessed_letters)
        acierto = juego.process_guess(letra)
        if acierto:
            print(f"¡Bien! La letra '{letra}' está en la palabra.")
        else:
            print(f"Fallaste. La letra '{letra}' no está.")

    # Mostrar estado final
    display_status(juego)
    print()
    if juego.is_won():
        print(f"¡Ganaste! La palabra era: {juego.word}")
    else:
        print(f"Fin del juego. La palabra era: {juego.word}")


if __name__ == "__main__":
    main()
