import matplotlib.pyplot as plt

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

fig, gnt = plt.subplots()

gnt.set_ylim(0, len(props)+1)
gnt.set_xlim(8, 20)

gnt.set_xlabel('Heures')
gnt.set_ylabel('Propositions')

ticks = []
ticks_label = []

for i in range(1, len(props)+2):
    if i < len(props)+1:
        ticks.append(i*50/len(props))
        ticks_label.append("Proposition " + str(i))
    else:
        ticks.append(i * 50 / len(props))
        ticks_label.append("Choix")

print(ticks)
print(ticks_label)

gnt.set_yticks(ticks)
gnt.set_yticklabels(ticks_label)

gnt.grid(True)

i = 0
while i < len(props):
    for el in props:
        print(el[0])
        print(el[-1])
        print(i)
        gnt.broken_barh([(el[0], el[-1])], (ticks[i], -2))
        i += 1

plt.savefig('gantt.png')
plt.show()