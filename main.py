from utils import get_random_word, get_valid_letter, display_status
from game import HangmanGame


def jugar_una_partida():
    """Ejecuta una partida completa y muestra el resultado."""
    palabra = get_random_word()
    juego = HangmanGame(palabra)

    while not juego.is_won() and not juego.is_lost():
        display_status(juego)
        letra = get_valid_letter(juego.guessed_letters)
        acierto = juego.process_guess(letra)
        if acierto:
            print(f"¡Bien! La letra '{letra}' está en la palabra.")
        else:
            print(f"Fallaste. La letra '{letra}' no está.")

    display_status(juego)
    print()
    if juego.is_won():
        print(f"¡Ganaste! La palabra era: {juego.word}")
    else:
        print(f"Fin del juego. La palabra era: {juego.word}")


def main():
    """
    Punto de entrada con bucle de replay.

    Envuelve una partida en jugar_una_partida() y pregunta si repetir.
    """
    while True:
        jugar_una_partida()
        # .strip().lower() normaliza para aceptar "S", "s", " s ".
        respuesta = input("¿Jugar otra partida? (s/n): ").strip().lower()
        # Solo salimos si escribió 'n'. Cualquier otra cosa reinicia.
        if respuesta == "n":
            print("¡Gracias por jugar!")
            break


if __name__ == "__main__":
    main()
