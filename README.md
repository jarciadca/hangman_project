# Hangman Project (Ahorcado)

Juego del ahorcado basado en consola. El jugador adivina letra por letra
una palabra o frase oculta dentro de un número limitado de intentos.

## Integrantes
- Joel Arcia (@jarciadca)
- Estela
- Cristian

## Reglas del juego
- Se adivina la frase letra por letra.
- Solo se aceptan letras como entrada válida.
- Cada intento incorrecto aumenta el contador de errores.
- Se pierde tras 6 intentos incorrectos.
- Se gana al adivinar todas las letras antes de agotar los intentos.
- Los caracteres no alfabéticos (espacios, guiones) se revelan automáticamente.

## Cómo ejecutar
```bash
python main.py