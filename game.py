"""
Módulo con la clase HangmanGame que encapsula el estado del juego.
"""


class HangmanGame:
    """
    Representa una partida del ahorcado.
    """

    def __init__(self, word):
        """Inicializa una nueva partida."""
        self.word = word
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        """
        Devuelve una cadena con el progreso actual de la palabra.
        Revela automáticamente los caracteres no alfabéticos (Tarea 7).
        """
        partes = []
        for caracter in self.word:
            # Si no es una letra (espacio, guion, etc.), se revela siempre.
            if not caracter.isalpha():
                partes.append(caracter)
            # Si es letra y ya fue adivinada, se muestra.
            elif caracter in self.guessed_letters:
                partes.append(caracter)
            # Si no, se oculta.
            else:
                partes.append("_")
        return " ".join(partes)

    def process_guess(self, letter):
        """
        Procesa una letra adivinada por el jugador (Tarea 4).
        """
        self.guessed_letters.append(letter)
        if letter in self.word:
            return True
        self.errors += 1
        return False

    def is_won(self):
        """Indica si el jugador ha ganado (Tarea 6)."""
        for caracter in self.word:
            if caracter.isalpha() and caracter not in self.guessed_letters:
                return False
        return True

    def is_lost(self):
        """Indica si el jugador ha perdido (Tarea 6)."""
        return self.errors >= self.max_errors
