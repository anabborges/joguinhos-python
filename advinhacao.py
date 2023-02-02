from random import randint

print('------------------------------------')
print('Seja bem vinde ao jogo da advinhação')
print('------------------------------------')

print('Escolha a dificuldade do seu jogo')

dificult = int(input('Digite: \n (1) para Fácil \n (2) para Médio \n (3) para Difícil '))

if dificult == 1:
    attempts = 20
elif dificult == 2:
    attempts = 10
else:
    attempts = 5

points = 1000
secret_number = randint(1,100)
number_tried = 0

while number_tried != secret_number and attempts != 0:
    print(f'Você tem {attempts} tentativas')
    number_tried = int(input('Digite um número de 1 a 100 '))
    if number_tried >= 1 and number_tried <= 100:
        if secret_number > number_tried:
            print('Dica: Tente chutar um número maior')
        elif secret_number < number_tried:
            print('Dica: Tente chutar um número menor')
        points -= abs(secret_number - number_tried)
        attempts -= 1
    elif number_tried > 100 or number_tried < 1:
        print('Você deve chutar um número de 1 a 100')
    print('------------------------')

if number_tried == secret_number:
    print('Parabéns! Você ganhou!')
    print(f'Você fez {points} pontos')
else:
    print(f'Você perdeu :( O número secreto era {secret_number}! Tente novamente')