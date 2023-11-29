def calculatrice():
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
            resultat = a + b
        elif choix == '2':
            resultat = a - b
        elif choix == '3':
            resultat = a * b
        elif choix == '4':
            if b != 0:
                resultat = a / b
            else:
                print("Erreur : division par zéro")
                continue
        else:
            print("Choix invalide. Veuillez entrer un numéro valide (1/2/3/4/5).")
            continue

        print("Le résultat de l'opération est:", resultat)

# Appel de la fonction de la calculatrice
calculatrice()
