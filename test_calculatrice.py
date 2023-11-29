def test_calculatrice():
    assert addition(3, 5) == 8
    assert soustraction(8, 3) == 5
    assert multiplication(3, 5) == 15

    # Test de division
    assert division(8, 2) == 4
    assert division(5, 0) == "Erreur : division par zéro"

    print("Tous les tests ont réussi !")

# Appel de la fonction de test
test_calculatrice()
