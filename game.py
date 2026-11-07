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
