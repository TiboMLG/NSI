from operator import itemgetter
from propositions import props

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

# Calcul des durées des locations
for el in props:
    el.append(el[1] - el[0])

# Tri selon la durée de la proposition, dans un odre décroissant
props = sorted(props, key=itemgetter(2), reverse=True)

# Liste des locations choisies. Ici avec l'heure de départ en indice 0 et l'heure de fin en indice 1
# Sous forme [[dbt des locations], [h de début, h de fin, laps de temps], [fin des locations]]
cluster = [[8, 8, 0], [20, 20, 0]]

cluster = acceptation(props, cluster)

print(props)  # Affichage des propositions
print(cluster)  # Affichage du choix final