# PyCharm version 2021.2.3
#
# Interpreteur python 3.10 preconfigure retrouvable en suivant le lien ci-dessous.
# https://tinyurl.com/o3yrmzt
#
# Par MALAGARIE-CAZENAVE Thibault
#
# Cet algorythme ne s'applique qu'avec un nombre de joueurs compris entre 1 et 6
#
# Certaines commandes de test se trouvent dans le programme sous forme de commentaires. Pour les activer, il suffit de
# supprimer les # les précédant

import random

""" creation du jeu """

Signe = ("carreau", "coeur", "trefle", "pique")
Valeur = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "valet", "dame", "roi", "As")

def creation(l_a, l_b):
    return [(x, y) for x in l_a for y in l_b]

Jeu = creation(Valeur, Signe)

# print("Liste du jeu:", Jeu)                    # Test du fonctionnement de la fonction creation(l_a, l_b)


""" shuffle """

def melange(jeu):
    return random.sample(jeu, 52)               # random.sample me permet de choisir le nombre de cartes utilisées

JeuShuffle = melange(Jeu)

# print("Jeu mélangé:", JeuShuffle)             #Test du fonctionnement de la fonction melange()


""" distribution """

Joueurs = None         # Nombre de joueurs
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
        for i in range(Joueurs):  # creation dynamique des variables se rapportant au nombre de joueurs (facultatif)
            globals()[f"J{i + 1}"] = []  # J1, J2, J3... suivant la valeur de la variable Joueurs

# print(globals())              # Test de la creation des variables

def distrib(jeu, joueurs):
    mains = [[] for joueurs in range(joueurs)]      # Creation de la liste des mains
    for k in range(len(jeu)//joueurs):
        for main in mains:
            main.append(jeu.pop(0))
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

BoolPrint = False

# Test de la valeur de la variable ChoixPrint

while BoolPrint is False:
    ChoixPrint = input("Voulez-vous afficher les mains des joueurs (non triées; si vous ne voulez pas les trier, elles "
                       "ne pourront plus être afficher)? Y/N").upper()
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


"""Tri des cartes"""

# Definition de "poids" à chaques cartes
DicCartes = {'2_pique': 1, '3_pique': 2, '4_pique': 3, '5_pique': 4, '6_pique': 5, '7_pique': 6, '8_pique': 7,
             '9_pique': 8, '10_pique': 9, 'valet_pique': 10, 'dame_pique': 11, 'roi_pique': 12, 'as_pique': 13,
             '2_carreau': 14, '3_carreau': 15, '4_carreau': 16, '5_carreau': 17, '6_carreau': 18, '7_carreau': 19,
             '8_carreau': 20, '9_carreau': 21, '10_carreau': 22, 'valet_carreau': 23, 'dame_carreau': 24,
             'roi_carreau': 25, 'as_carreau': 26, '2_coeur': 27, '3_coeur': 28, '4_coeur': 29, '5_coeur': 30,
             '6_coeur': 31, '7_coeur': 32, '8_coeur': 33, '9_coeur': 34, '10_coeur': 35, 'valet_coeur': 36,
             'dame_coeur': 37, 'roi_coeur': 38, 'as_coeur': 39, '2_trefle': 40, '3_trefle': 41, '4_trefle': 42,
             '5_trefle': 43, '6_trefle': 44, '7_trefle': 45, '8_trefle': 46, '9_trefle': 47, '10_trefle': 48,
             'valet_trefle': 49, 'dame_trefle': 50, 'roi_trefle': 51, 'as_trefle': 52}

# Attribution des cartes à leur poids
def poids_cartes(val):
    return DicCartes[str.lower(str(val[0])+"_"+val[1])]

# Fonction de tri des mains suivant leur poids
def tri_main(main):
    return sorted(main, key=poids_cartes)

# Choix du tri des mains
BoolTri = False

while BoolTri is False:
    ChoixTri = input("Voulez-vous trier les mains des joueurs? Y/N").upper()
    if ChoixTri == "Y":
        BoolTri = True
        if Joueurs == 1:
            J1T = tri_main(J1)
        elif Joueurs == 2:
            J1T = tri_main(J1)
            J2T = tri_main(J2)
        elif Joueurs == 3:
            J1T = tri_main(J1)
            J2T = tri_main(J2)
            J3T = tri_main(J3)
        elif Joueurs == 4:
            J1T = tri_main(J1)
            J2T = tri_main(J2)
            J3T = tri_main(J3)
            J4T = tri_main(J4)
        elif Joueurs == 5:
            J1T = tri_main(J1)
            J2T = tri_main(J2)
            J3T = tri_main(J3)
            J4T = tri_main(J4)
            J5T = tri_main(J5)
        else:
            J1T = tri_main(J1)
            J2T = tri_main(J2)
            J3T = tri_main(J3)
            J4T = tri_main(J4)
            J5T = tri_main(J5)
            J6T = tri_main(J6)
    elif ChoixTri == "N":
        BoolTri = True
        print("Les mains des joueurs n'ont pas été triées")
    else:
        BoolTri = False
        print("Le choix doit être soit N (No), soit Y (Yes).")

# Choix de l'affichage des mains triees

BoolPrint = False

if ChoixTri == "Y":
    while BoolPrint is False:
        ChoixPrint = input("Voulez-vous afficher les mains triées des joueurs? Y/N").upper()
        if ChoixPrint == "Y":
            BoolPrint = True
            if Joueurs == 1:
                print("Joueur 1:", J1T)
            elif Joueurs == 2:
                print("Joueur 1:", J1T)
                print("Joueur 2:", J2T)
            elif Joueurs == 3:
                print("Joueur 1:", J1T)
                print("Joueur 2:", J2T)
                print("Joueur 3:", J3T)
            elif Joueurs == 4:
                print("Joueur 1:", J1T)
                print("Joueur 2:", J2T)
                print("Joueur 3:", J3T)
                print("Joueur 4:", J4T)
            elif Joueurs == 5:
                print("Joueur 1:", J1T)
                print("Joueur 2:", J2T)
                print("Joueur 3:", J3T)
                print("Joueur 4:", J4T)
                print("Joueur 5:", J5T)
            else:
                print("Joueur 1:", J1T)
                print("Joueur 2:", J2T)
                print("Joueur 3:", J3T)
                print("Joueur 4:", J4T)
                print("Joueur 5:", J5T)
                print("Joueur 6:", J6T)
        elif ChoixPrint == "N":
            BoolPrint = True
            print("Les mains triées des joueurs n'ont pas été affichées")
        else:
            BoolPrint = False
            print("Le choix doit être soit N (No), soit Y (Yes).")

# Affichage du pot
if len(Pot) == 0:
    print("Il n'y a pas de cartes dans le pot")
else:
    print("Les cartes dans le pot sont:", Pot)
    
