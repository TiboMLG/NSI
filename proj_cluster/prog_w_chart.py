from operator import itemgetter
import matplotlib.pyplot as plt


# FONCTIONS

# Fonction qui permet de sélectionner les locations
def acceptation(propositions, agenda):
    # Insertions des plus grandes plages horaires
    agenda.insert(1, propositions[0])
    propositions.pop(0)
    for l in propositions:
        if l[0] >= agenda[-2][1]:
            agenda.insert(-1, l)
            propositions.remove(l)

    # Choix des plages horaires qui conviennent à celles sélectionnées auparavant
    for k in range(1, len(agenda)):
        if agenda[k - 1][1] - agenda[k][0] != 0:  # Test pour connaître s'il y a un espace entre deux réservations
            for p in propositions:
                if p[0] >= agenda[k - 1][1] and p[1] <= agenda[k][0]:  # Test pour connaître la "meilleure" réservation à sélectionner
                    agenda.insert(k, p)  # Ajout de la réservation
                    propositions.remove(p)  # Suppression de celle-ci aux propositions
    return agenda


# Propositions de locations
props = [[8, 10],
         [8, 9],
         [8, 12],
         [9, 15],
         [9, 13],
         [11, 14],
         [13, 15],
         [14, 17],
         [16, 17],
         [16, 18],
         [17, 20],
         [19, 20]
         ]

# Calcul des durées des locations
for el in props:
    el.append(el[1] - el[0])


# CREATION DU GRAPHIQUE GANTT

fig, gnt = plt.subplots()

# Définition des limites du graphique
gnt.set_ylim(0, len(props) + 1)
gnt.set_xlim(8, 20)

# Légende
gnt.set_xlabel('Heures')
gnt.set_ylabel('Propositions')

# Création des points de référence
ticks = []  # Liste comprennant les coordonnées des ticks
ticks_label = []    # Liste comprennant les noms des ticks

for i in range(1, len(props) + 2):
    if i < len(props) + 1:
        ticks.append(i * 50 / len(props))
        ticks_label.append("Proposition " + str(i))
    else:
        ticks.append(i * 50 / len(props))
        ticks_label.append("Choix")

gnt.set_yticks(ticks)   # Assignation des ticks
gnt.set_yticklabels(ticks_label)    # Assignation des noms des ticks

gnt.grid(True)  # Affichage de la grille

# Placement des propositions de location
i = 0
while i < len(props):
    for el in props:
        gnt.broken_barh([(el[0], el[-1])], (ticks[i], -2))
        i += 1

# Tri selon la durée de la proposition, dans un odre décroissant
props = sorted(props, key=itemgetter(2), reverse=True)

# Liste des locations choisies. Ici avec l'heure de départ en indice 0 et l'heure de fin en indice 1
cluster = [[8, 8, 0], [20, 20, 0]]

cluster = acceptation(props, cluster)

print(props)  # Affichage des propositions
print(cluster)  # Affichage du choix final

# Liste des couleurs utilisables
colours = ['blue', 'red', 'green', 'cyan', 'black', 'magenta', 'yellow']

# Ajout des locations sélectionnées au graphique
i = 0
for loc in cluster:
    gnt.broken_barh([(loc[0], loc[-1])], (ticks[-1], -2), facecolors=colours[i])
    i += 1

plt.savefig('gantt.png')    # Sauvegarde du graphique
plt.show()  # Affichage du graphique
