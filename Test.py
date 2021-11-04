Joueurs = None
BoolJ = False          # Variable de test pour la valeur de la variable Joueurs

# Test de la valeur de la variable Joueur

while BoolJ is False:
    Joueurs = ""
    # Verification que la valeur entree est bien un nombre
    while Joueurs.isdigit() is not int:
        try:
            Joueurs = int(input("Combien y a-t-il de joueurs?"))
            break
        except ValueError:
            print("Veuillez entrer un nombre entier: ")
    # Verification que la valeur entree se trouve entre 1 et 6
    if int(Joueurs) > 6 or int(Joueurs) < 0:
        BoolJ = False
        print("Le nombre de joueurs doit être compris entre 1 et 6.")
    else:
        BoolJ = True
        for i in range(Joueurs):                   # creation dynamique des variables se rapportant au nombre de joueurs
            globals()[f"J{i + 1}"] = []            # J1, J2, J3... suivant la valeur de la variable Joueurs
