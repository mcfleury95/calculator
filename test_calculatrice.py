from calculatrice import addition, soustraction, multiplication, division

# Test d'addition
assert addition(3, 5) == 8
assert addition(-1, 1) == 0
assert addition(0, 0) == 0

# Test de soustraction
assert soustraction(8, 3) == 5
assert soustraction(-1, 1) == -2
assert soustraction(0, 0) == 0

# Test de multiplication
assert multiplication(3, 5) == 15
assert multiplication(-1, 1) == -1
assert multiplication(0, 0) == 0

# Test de division
assert division(8, 2) == 4
assert division(-6, 3) == -2
assert division(0, 5) == 0

# Test de division par zéro
assert division(5, 0) == "Erreur : division par zéro"

print("Tous les tests ont réussi !")
