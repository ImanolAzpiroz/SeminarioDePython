import random


print(f"Nota: Podria haber modularizado. \U0001F616")

words_dic = {
    "Fulbo" : ["independiente", "river", "boca", "racing", "huracan"],
    "Series" : ["breaking", "thrones", "jujutsu", "shingeki", "mandalorian"],
    "Top 5 mejores guitarristas" : ["gardiner", "wong", "henson", "danel", "zytecki", "rafa", "poniaseisno"],
    "Placebos" : ["nada", "vacio", "cero", "nulo"],
    "Standard" : ["python", "programa", "variable", "funcion", "bucle", "cadena", "entero", "lista"]
}

guessed = []
attempts = 6
points = 0
keep_playing = "s"
same_category = "n"
index = 0

while keep_playing == "s":

    print("¡Bienvenido al Ahorcado!")
    print()

    if same_category == "n":
        # Interfaz para seleccionar categoría (Usa enumerate para poder usar un indice en la seleccion)
        print("Seleccione una categoria: ")
        for i, category in enumerate(words_dic.keys(), 1):
            print(f"{i}. {category}")

        category_index = int(input())

        # (Lo hice de nuevo por que no me quedo claro del todo)
        # Lista de categorias:
        categories = list(words_dic.keys())
        # Con el indice ingresado accedemos a la categoria elegiad
        chosen_category = categories[category_index - 1]

        print(f"La categoria elegida es: {chosen_category}")

        random_choise_no_repeat = random.sample(words_dic[chosen_category], len(words_dic[chosen_category]))
        #print(random_choise_no_repeat)
        index = 0

    if index < len(random_choise_no_repeat):
        word = random_choise_no_repeat[index]
        index += 1
    else:
        print("No quedan mas palabras en esta categoria.")


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

    keep_playing = input("Jugar otra ronda? (s/n): ").lower()
    if keep_playing == "s":
        # Reiniciar el juego
        guessed = []
        attempts = 6
        points = 0
        same_category = input("Misma categoria? (s/n): ").lower()

        print(keep_playing)
        print(same_category)
    else:
        print("¡Gracias por jugar!")


