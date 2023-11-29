def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : division par zéro"

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

    a = float(input("Entrez le premier nombre: "))
    b = float(input("Entrez le deuxième nombre: "))

    if choix == '1':
        resultat = addition(a, b)
    elif choix == '2':
        resultat = soustraction(a, b)
    elif choix == '3':
        resultat = multiplication(a, b)
    elif choix == '4':
        resultat = division(a, b)
    else:
        print("Choix invalide. Veuillez entrer un numéro valide (1/2/3/4/5).")
        continue

    print("Le résultat de l'opération est:", resultat)

