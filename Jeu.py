# PyCharm version 2021.2.3
#
# Interpreteur python 3.10 preconfigure retrouvable en suivant le lien ci-dessous.
# https://tinyurl.com/o3yrmzt
#
# Par MALAGARIE-CAZENAVE Thibault
#
# Programme realise dans le cadre des cours de NSI
#
# Cet algorythme ne s'applique qu'avec un nombre de joueurs compris entre 1 et 6
#
# La dernière ligne peut créer une erreur selon l'interpreteur utilise. Si cela se passe, ce n'est pas un
# problème, l'algorythme s'arrête dans tous les cas et cette lignes permet seulement qu'il s'arrête proprement. Elle peut aussi être supprimée
#
# Certaines commandes de test se trouvent dans le programme sous forme de commentaires. Pour les activer, il suffit de
# supprimer les # les précédant
#
# Derniere modification le 04/11 à 15h30

import random

""" creation du jeu """

signe = ("carreau", "coeur", "trefle", "pique")
valeur = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "valet", "dame", "roi", "As")

def creation():
    return [(x, y) for x in valeur for y in signe]

Jeu = creation()

# print(Jeu)                    # Test du fonctionnement de la fonction melange()


""" shuffle """

def melange():
    return random.sample(Jeu, 52)

JeuShuffle = melange()

# print(JeuShuffle)             #Test du fonctionnement de la fonction melange()


""" distribution """

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
            print("Veuillez entrer un nombre entier.")
    # Verification que la valeur entree se trouve entre 1 et 6
    if int(Joueurs) > 6 or int(Joueurs) < 0:
        BoolJ = False
        print("Le nombre de joueurs doit être compris entre 1 et 6.")
    else:
        BoolJ = True
        for i in range(Joueurs):  # creation dynamique des variables se rapportant au nombre de joueurs
            globals()[f"J{i + 1}"] = []  # J1, J2, J3... suivant la valeur de la variable Joueurs

# print(globals())              # Test de la creation des variables

def distrib(jeu, joueurs):
    mains = [[] for joueurs in range(joueurs)]
    for i in range(len(jeu)//joueurs):
        for main in mains:
            main.append(JeuShuffle.pop(0))
    return mains
Pot = JeuShuffle
Mains = distrib(JeuShuffle, Joueurs)

if Joueurs == 2:           # assignement des mains aux differents joueurs en fonction du nombre de ceux-ci
    J1 = Mains[0]
    J2 = Mains[1]
elif Joueurs == 3:
    J1 = Mains[0]
    J2 = Mains[1]
    J3 = Mains[2]
elif Joueurs == 4:
    J1 = Mains[0]
    J2 = Mains[1]
    J3 = Mains[2]
    J4 = Mains[3]
elif Joueurs == 5:
    J1 = Mains[0]
    J2 = Mains[1]
    J3 = Mains[2]
    J4 = Mains[3]
    J5 = Mains[4]
elif Joueurs == 6:
    J1 = Mains[0]
    J2 = Mains[1]
    J3 = Mains[2]
    J4 = Mains[3]
    J5 = Mains[4]
    J6 = Mains[5]
else:
    J1 = Mains[0]


"""Choix de l'affichage des mains des joueurs"""

ChoixPrint = None
BoolPrint = False

# Test de la valeur de la variable ChoixPrint

while BoolPrint is False:
    ChoixPrint = input("Voulez-vous afficher les mains des joueurs? Y/N").upper()
    if ChoixPrint == "Y":
        BoolPrint = True
        if Joueurs == 1:
            print("Joueur 1:", J1)
        elif Joueurs == 2:
            print("Joueur 1:", J1)
            print("Joueur 2:", J2)
        elif Joueurs == 3:
            print("Joueur 1:", J1)
            print("Joueur 2:", J2)
            print("Joueur 3:", J3)
        elif Joueurs == 4:
            print("Joueur 1:", J1)
            print("Joueur 2:", J2)
            print("Joueur 3:", J3)
            print("Joueur 4:", J4)
        elif Joueurs == 5:
            print("Joueur 1:", J1)
            print("Joueur 2:", J2)
            print("Joueur 3:", J3)
            print("Joueur 4:", J4)
            print("Joueur 5:", J5)
        else:
            print("Joueur 1:", J1)
            print("Joueur 2:", J2)
            print("Joueur 3:", J3)
            print("Joueur 4:", J4)
            print("Joueur 5:", J5)
            print("Joueur 6:", J6)
    elif ChoixPrint == "N":
        BoolPrint = True
        print("Les mains des joueurs n'ont pas été affichées")
    else:
        BoolPrint = False
        print("Le choix doit être soit N (No), soit Y (Yes).")

if len(Pot) == 0:                                       # affichage du pot
    print("Il n'y a pas de cartes dans le pot")
else:
    print("Les cartes dans le pot sont:", Pot)

exit()
