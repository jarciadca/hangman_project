"""
Módulo con la clase HangmanGame que encapsula el estado del juego.

Modela la palabra objetivo, las letras adivinadas, el límite de errores
y el conteo actual de errores del jugador.

Autor original: Joel (Tarea 2)
Contribuciones: Estela (Tarea 4), Cristian (Tareas 6 y 7)
Curso: Desarrollo de Software con IA
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

        Args:
            word (str): palabra objetivo ya normalizada a minúsculas.
        """
        # Guardamos la palabra como atributo de instancia.
        # 'self.' porque cada objeto tiene SU propia palabra.
        self.word = word

        # Lista vacía para letras ya adivinadas.
        # Lista (no set) porque el enunciado lo pide y conserva orden.
        self.guessed_letters = []

        # Límite de errores fijo según reglas del juego (6).
        self.max_errors = 6

        # Contador de errores arranca en 0.
        self.errors = 0

    def display_progress(self):
        """
        Devuelve una cadena con el progreso actual de la palabra.

        Letras adivinadas se muestran tal cual; no adivinadas como '_'.
        Caracteres no alfabéticos (espacios, guiones) se revelan siempre
        (Tarea 7), porque el jugador no puede adivinarlos: get_valid_letter
        solo acepta letras.

        Returns:
            str: representación visual del estado de la palabra.
        """
        # 'partes' acumula símbolos; lista + join es O(n).
        # Concatenar con '+=' en bucle sería O(n²) por inmutabilidad de str.
        partes = []

        # Recorremos la PALABRA (no guessed_letters) para respetar
        # orden original y repeticiones (ej. 'banana' tiene 3 'a').
        for caracter in self.word:
            # CAMBIO TAREA 7: si NO es letra (espacio, guion...), se revela
            # SIEMPRE. Este 'if' va PRIMERO para tener prioridad sobre la
            # lógica de "adivinada o no" de abajo.
            if not caracter.isalpha():
                partes.append(caracter)
            # Letra ya adivinada: se muestra.
            elif caracter in self.guessed_letters:
                partes.append(caracter)
            # Letra no adivinada: se oculta.
            else:
                partes.append("_")

        # ' '.join(lista) une con espacio → "_ _ e _ _ a _ _".
        return " ".join(partes)

    def process_guess(self, letter):
        """
        Procesa una letra adivinada por el jugador (Tarea 4).

        Agrega la letra a guessed_letters (se haya acertado o no),
        incrementa errors si es incorrecta y devuelve si acertó.

        Args:
            letter (str): letra ya validada y en minúsculas.

        Returns:
            bool: True si la letra estaba en la palabra, False si no.
        """
        # Agregamos SIEMPRE al historial: la Tarea 5 exige mostrar
        # letras intentadas incluyendo las incorrectas.
        self.guessed_letters.append(letter)

        # 'in' verifica pertenencia (O(n) sobre str). Comparación directa
        # porque ambos están en minúsculas (validado en get_valid_letter).
        if letter in self.word:
            return True

        # Fallo: incrementamos contador.
        self.errors += 1
        return False

    def is_won(self):
        """
        Indica si el jugador ha ganado la partida (Tarea 6).

        Gana cuando todas las letras alfabéticas de la palabra han sido
        adivinadas. Los no alfabéticos (espacios, guiones) se ignoran,
        porque get_valid_letter nunca los permite adivinar.

        Returns:
            bool: True si todas las letras alfabéticas están adivinadas.
        """
        # Recorremos cada carácter de la palabra.
        for caracter in self.word:
            # Solo consideramos letras: espacios/guiones se revelan solos
            # (Tarea 7) y no bloquean la victoria.
            if caracter.isalpha() and caracter not in self.guessed_letters:
                # Letra pendiente → no ganó. Cortocircuito.
                return False

        # Sin pendientes → todas adivinadas.
        return True

    def is_lost(self):
        """
        Indica si el jugador ha perdido la partida (Tarea 6).

        Pierde cuando errors alcanza o supera max_errors.

        Returns:
            bool: True si errors >= max_errors.
        """
        # '>=' defensivo: si errors saltara por bug, igual detecta derrota.
        return self.errors >= self.max_errors
