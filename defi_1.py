# On demande 3 valeurs à l'utilisateur
val1 = int(input("Donne-moi une valeur entière : "))
val2 = int(input("Donne-moi une deuxième valeur entière : "))
val3 = int(input("Donne-moi une troisième valeur entière : "))

# On les met dans une liste
L = [val1, val2, val3]
print("Ta liste de départ est :", L)

# On demande les positions à permuter
pos1 = int(input("Choisis le numéro (1, 2 ou 3) de la première valeur à permuter : ")) - 1
pos2 = int(input("Choisis le numéro (1, 2 ou 3) de la deuxième valeur à permuter : ")) - 1

# On permute les valeurs
L[pos1], L[pos2] = L[pos2], L[pos1]

# On affiche le résultat
print("Ta nouvelle liste est :", L)
