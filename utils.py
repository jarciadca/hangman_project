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
