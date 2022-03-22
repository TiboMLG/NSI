from random import randint

nbr = randint(0, 100)
print(nbr)

max = int(input("Nombre entre 0 et:"))
probs = [i for i in range(max)]
probs = [i for i in range(max)]

guess = probs[round(len(probs)/2)+1]

while guess != nbr:
    if guess > nbr:
        probs = probs[:len(probs)//2]
        if len(probs) == 2 or len(probs) == 1:
            guess = probs[0]
        else:
            guess = probs[len(probs)//2]

    else:
        probs = probs[len(probs)//2:]
        if len(probs) == 2 or len(probs) == 1:
            guess = probs[0]
        else:
            guess = probs[len(probs) // 2]

print(guess)