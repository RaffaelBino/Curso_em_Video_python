from random import randint as rdi
from time import sleep
# Exercicio 28
print('='*20, 'Primeiro exercicio','='*20)
pc = rdi(0, 5)  # faz o computador sortear unm número
print('-=-' * 25)
sleep(.5)
print('Vou pensar em um número entre 0 e 5, tente advinhar !')
sleep(.5)
print('-=-' * 25)
sleep(.5)
jogador = int(input('Em que número em pensei ? '))  # Jogador tenta advinhar
print('Processando...')
sleep(2)
if jogador == pc:
    print('Parabéns, o número {} foi o que eu realmente pensei'.format(jogador))
else:
    print('Infelizmente você errou, eu pensei no número {} e não no {}.'.format(pc, jogador))

# Exercicio 29
print('='*20, 'Segundo exercicio','='*20)
vel = float(input('Qual a velocidade atual do seu carro? '))
mult = (vel - 80) * 7
if vel > 80:
    print('Você foi multado, você excedeu o limite de velocidade de 80Km/h')
    sleep(.3)
    print('Você deve pagar uma multa no valor de R${:.2f}'.format(mult))
else:
    print('OK! Diriga com cuidado!')

# Exercicio 30
print('='*20, 'Terceiro exercicio','='*20)
n = int(input('Me diga um número: '))
if n % 2 == 0:
    print('O  número {} é Par'.format(n))
else:
    print('O número {} é Ímpar'.format(n))

# Exercicio 30
print('='*20, 'Terceiro exercicio','='*20)
