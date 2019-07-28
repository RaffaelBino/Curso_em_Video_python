from random import randint as rdi
from time import sleep
from datetime import date
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

# Exercicio 31
print('='*20, 'Quarto exercicio','='*20)
dist = float(input('Quantos Km é sua viagem ? '))
print('Você está prestes a começar a sua viagem de {}Km.'.format(dist))
if dist <= 200:
    valp = dist * 0.50
else:
    valp = dist * 0.45
print('E o preço da sua passagem será: R${:.2f}'.format(valp))

# Exercicio 32
print('='*20, 'Quinto exercicio','='*20)
ano = int(input('Qual ano você quer analisar? Coloque 0 para analisar o ano atual. -> '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
