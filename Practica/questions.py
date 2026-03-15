import random

words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]

word = random.choice(words)
guessed = []
attempts = 6

points = 0

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
# Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)


    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        points += 6
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    user_input = input("Ingresá una letra: ")

    # Validar que el input sea una sola letra y no un número o símbolo
    if len(user_input) != 1 or not user_input.isalpha():
        print("Entrada no valida")
        continue

    if user_input in guessed:
        print("Ya usaste esa letra.")
    elif user_input in word:
        guessed.append(user_input)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(user_input)
        attempts -= 1
        print("Esa letra no está en la palabra.")
        points -= 1

    print()

else:
    print(f"¡Perdiste! La palabra era: {word}")
    points = 0

print(f"Puntaje final: {points}")
