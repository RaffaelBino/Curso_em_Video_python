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

# Exercicio 33
print('='*20, 'Sexto exercicio','='*20)
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))
if n1 > n2 and n1 > n3:
    print('O maior valor é o {} '.format(n1))
if n2 > n1 and n2 > n3:
    print('O maior valor é o {} '.format(n2))
if n3 > n1 and n3 > n2:
    print('O maior valor é o {} '.format(n3))
if n1 < n3 and n1 < n2:
    print('O menor valor {}'.format(n1))
if n2 < n3 and n2 < n1:
    print('O menor valor {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('O menor valor {}'.format(n3))

# Exercicio 34
print('='*20, 'Sétimo exercicio','='*20)
sal = float(input('Qual o seu salário atual ? R$'))
if sal > 1250:
    sal = sal + (sal * (10/100))
    print('Seu salário passou a ser R${:.2f}'.format(sal))
else:
    sal = sal + (sal * (15/100))
    print('Seu salário passou a ser R${:.2f}'.format(sal))

# Exercicio 35
print('='*20, 'Oitavo exercicio','='*20)
print('-=-' * 25)
sleep(.5)
print('ANÁLISADOR DE TRIANGULOS')
sleep(.5)
print('-=-' * 25)
s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os seguimentos acima pode formar Triangulo')
else:
    print('Os seguimentos acima não podem formar Triangulo')
