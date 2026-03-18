import random
import sys

words_dic = {
    "Fulbo" : ["independiente", "river", "boca", "racing", "huracan"],
    "Series" : ["breaking", "thrones", "jujutsu", "shingeki", "mandalorian"],
    "Top5 mejores guitarristas" : ["gardiner", "wong", "henson", "danel", "zytecki", "rafa", "poniaseisno"],
    "Placebos" : ["nada", "vacio", "cero", "nulo"],
    "Standard" : ["python", "programa", "variable", "funcion", "bucle", "cadena", "entero", "lista"]
}

guessed = []
attempts = 6

points = 0

print("¡Bienvenido al Ahorcado!")
print()

# Interfaz para seleccionar categoría (Usa enumerate para poder usar un indice en la seleccion)
print("Seleccione una categoria: ")
for i, category in enumerate(words_dic.keys(), 1):
    print(f"{i}. {category}")

category_choice = int(input())

# (Lo hice de nuevo por que no me quedo claro del todo)
# Lista de categorias:
categories = list(words_dic.keys())
# Con el indice ingresado accedemos a la categoria elegiad
cat_elegida = categories[category_choice - 1]
# Ahora el indice es un str, y podemos acceder al diccionario para obtener la palabra a adivinar, sobre eso hacemos el random
word = random.choice(words_dic[cat_elegida])

print(f"La categoria elegida es: {cat_elegida}")

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
        print()
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
