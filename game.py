"""
Módulo con la clase HangmanGame que encapsula el estado del juego.

Modela la palabra objetivo, las letras adivinadas, el límite de errores
y el conteo actual de errores del jugador.
"""


class HangmanGame:
    """
    Representa una partida del ahorcado.

    Attributes:
        word (str): palabra o frase objetivo a adivinar.
        guessed_letters (list[str]): letras ya intentadas por el jugador.
        max_errors (int): número máximo de fallos permitidos (6).
        errors (int): cantidad de fallos cometidos hasta ahora.
    """

    def __init__(self, word):
        """
        Inicializa una nueva partida.
        """
        self.word = word

        self.guessed_letters = []

        self.max_errors = 6

        self.errors = 0

    def display_progress(self):
        """
        Devuelve una cadena con el progreso actual de la palabra.

        Letras adivinadas se muestran tal cual; no adivinadas como '_'.
        Caracteres separados por espacio para legibilidad.

        Retorna:
            str: representación visual del estado de la palabra.
        """
        partes = []

        for caracter in self.word:
            if caracter in self.guessed_letters:
                partes.append(caracter)
            else:
                partes.append("_")

        return " ".join(partes)

    def is_won(self):
        """
        Indica si el jugador ha ganado la partida.

        Gana cuando todas las letras alfabéticas de la palabra han sido
        adivinadas. Los no alfabéticos (espacios, guiones) se ignoran.

        Returns:
            bool: True si todas las letras alfabéticas están adivinadas.
        """
        for caracter in self.word:
            if caracter.isalpha() and caracter not in self.guessed_letters:
                return False
        return True

    def is_lost(self):
        """
        Indica si el jugador ha perdido la partida.

        Pierde cuando errors alcanza o supera max_errors.

        Returns:
            bool: True si errors >= max_errors.
        """
        return self.errors >= self.max_errors
