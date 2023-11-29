def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Erreur : division par zéro"

# Menu principal
while True:
    print("Sélectionnez une opération:")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

    choix = input("Entrez le numéro de l'opération souhaitée (1/2/3/4/5): ")

    if choix == '5':
        print("Au revoir !")
        break

    nombre1 = float(input("Entrez le premier nombre: "))
    nombre2 = float(input("Entrez le deuxième nombre: "))

    if choix == '1':
        print(nombre1, "+", nombre2, "=", addition(nombre1, nombre2))

    elif choix == '2':
        print(nombre1, "-", nombre2, "=", soustraction(nombre1, nombre2))

    elif choix == '3':
        print(nombre1, "*", nombre2, "=", multiplication(nombre1, nombre2))

    elif choix == '4':
        print(nombre1, "/", nombre2, "=", division(nombre1, nombre2))

    else:
        print("Choix invalide. Veuillez entrer un numéro valide (1/2/3/4/5).")