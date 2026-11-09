"""
Módulo de funciones auxiliares para el juego del ahorcado.
"""

import random

WORDS_FILE = "wordlist.txt"


def get_random_word():
    """
    Devuelve una palabra o frase aleatoria cargada desde wordlist.txt.
    """
    with open(WORDS_FILE, "r", encoding="utf-8") as file:
        words = [
            line.strip().lower()
            for line in file.readlines()
            if line.strip() and any(c.isalpha() for c in line)
        ]

    if not words:
        raise ValueError(
            f"El archivo {WORDS_FILE} no contiene palabras válidas."
        )

    return random.choice(words)


def get_valid_letter(guessed_letters):
    """
    Pide una letra al jugador hasta recibir una entrada válida.

    Acepta exactamente un carácter alfabético que no esté en
    guessed_letters. Si la entrada no es válida, muestra el motivo
    y vuelve a pedirla.
    """
    while True:
        entry = input("Ingresa una letra: ").strip().lower()
        if len(entry) != 1:
            print("Error: debes ingresar exactamente una letra.")
        elif not entry.isalpha():
            print("Error: debes ingresar una letra.")
        elif entry in guessed_letters:
            print(f"Error: Ya intentaste la letra '{entry}'.")
        else:
            return entry


def display_status(game):
    """
    Muestra el estado actual de la partida.

    Imprime el progreso de la palabra, las letras ya intentadas
    (correctas e incorrectas) y los intentos incorrectos restantes.
    """
    attempted = ", ".join(sorted(game.guessed_letters)) or "-"
    remaining = game.max_errors - game.errors

    print()
    print(f"Palabra: {game.display_progress()}")
    print(f"Letras intentadas: {attempted}")
    print(f"Intentos restantes: {remaining}")


# Lista de 7 dibujos ASCII del ahorcado, indexados por errores.
# Índice 0 = sin errores, índice 6 = completo. Lista (no dict) porque
# el índice ES el número de errores → lookup O(1) directo.
HANGMAN_ART = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
]


def display_hangman(errors):
    """
    Muestra el dibujo ASCII del ahorcado según los errores cometidos.

    Args:
        errors (int): número de errores actuales (0 a 6).
    """
    # Clamp defensivo: si errors superara 6, usamos el último dibujo.
    # min() evita IndexError.
    indice = min(errors, len(HANGMAN_ART) - 1)
    print(HANGMAN_ART[indice])
