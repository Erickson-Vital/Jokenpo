#Jogo de Jokenpo simples feito em python
#Jogo desenvolvido no curso de python - Curso em Video

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Faça sua jogada!:
[0] Pedra
[1] Papel
[2] Tesoura

''')
jogador = int(input('Qual será sua jogada ? ?'))

print('O computador escolheu {}'.format(itens[computador]))