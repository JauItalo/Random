import random


def adivinhe_computador(x):
    baixo = 1
    alto = x
    feedback = ''
    while feedback != 'c':
        if baixo != alto:
            adivinhe = random.randint(baixo, alto)
        else:
            adivinhe = baixo
        feedback = input(f'O {adivinhe} é muito alto (A), muito baixo (B) ou correto (C)??').lower()
        if feedback == 'a':
            alto = adivinhe - 1
        elif feedback == 'b':
            baixo = adivinhe + 1

    print(f'AEE! O computador adivinhou o seu numero, {adivinhe_computador}!')

adivinhe_computador(10)

