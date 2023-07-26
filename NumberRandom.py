import random

def adivinhe(x):
    random_n = random.randint(1, x)
    adivinhe = 0
    while adivinhe != random_n:
        adivinhe = int(input(f'Adivinhe um numero entre 1 e {x}: '))
        if adivinhe < random_n:
            print('My bad, tente novamente. Muito baixo.')
        elif adivinhe > random_n:
            print('My bad, tente novamente. Muito alto.')

    print(f"Aeee, parabéns. VoCê adivinhou o número aleatorio era {random_n}")


adivinhe(10)

