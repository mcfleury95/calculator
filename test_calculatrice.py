def calculatrice():
    assert addition(3, 5) == 8
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0

    assert soustraction(8, 3) == 5
    assert soustraction(-1, 1) == -2
    assert soustraction(0, 0) == 0

    assert multiplication(3, 5) == 15
    assert multiplication(-1, 1) == -1
    assert multiplication(0, 0) == 0

    assert division(8, 2) == 4
    assert division(-6, 3) == -2
    assert division(0, 5) == 0

    assert division(5, 0) == "Erreur : division par zéro"

    print("Tous les tests ont réussi !")

# Appel de la fonction de test
calculatrice()
