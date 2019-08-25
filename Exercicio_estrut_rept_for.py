from datetime import date
from time import sleep
# Exercicio 46
print('=' * 20, 'Primeiro exercicio', '=' * 20)
for i in range(10, -1, -1):
    print(i)
    sleep(.5)
print('FELIZ ANO NOVO!!!')

# Exercicio 47
print('=' * 20, 'Segundo exercicio', '=' * 20)
for i in range(0, 51, 2):
    # for i in range(0, 51):
    #    if i % 2 == 0:
    print(i, end=' ')
print('Acabou')

# Exercicio 48
print('=' * 20, 'Terceiro exercicio', '=' * 20)
soma = 0
cont = 0
for i in range(1, 501):
    if i % 3 == 0:
        cont += 1
        soma += i
print('A soma dos {} valores solicitados é {}.'.format(cont, soma))

# Exercicio 49
print('=' * 20, 'Quarto exercicio', '=' * 20)
n = int(input('Digite um numero de 1 a 9 para saber sua tábuada: '))
for i in range(1, 11):
    print('{} x {:2} = {}'.format(n, i, n*i))

# Exercicio 50
print('=' * 20, 'Quinto exercicio', '=' * 20)
som = 0
for i in range(1, 7):
    num = int(input('Digite o {} valor: '.format(i)))
    if num % 2 == 0:
        som += num
print('A soma de todos os valores pares é: {}.'.format(som))

# Exercicio 51
print('=' * 20, 'Sexto exercicio', '=' * 20)
x = int(input('Primeiro termo:  '))
y = int(input('Razao: '))
decimo = x + (10 - 1) * y
for i in range(x, decimo + y, y):
    print('{}'.format(i), end='-> ')
print('Acabou')

# Exercicio 52
print('=' * 20, 'Setimo exercicio', '=' * 20)
nump = int(input('Digite um número: '))
tot = 0
for i in range(1, nump + 1):
    if nump % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(i), end=' ')
print('\n\033[0mO número {} foi divisível {} vezes'.format(nump, tot))
if tot == 2:
    print('E por isso ele é Primo!')
else:
    print('E por isso ele não é Primo!')

# Exercicio 53
print('=' * 20, 'Oitavo exercicio', '=' * 20)
frase = str(input('Digite uma frase')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
# inverso  = junto[::-1]
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um pálindromo!')
else:
    print('A frase digitada não é um palíndromo!')

# Exercicio 54
print('=' * 20, 'Nono exercicio', '=' * 20)
atual = date.today().year
velho = 0
novo = 0
for i in range(1, 8):
    ano = int(input('Em que ano a {}º pessoa nasceu ? '.format(i)))
    idade = atual - ano
    if idade >= 21:
        velho += 1
    else:
        novo += 1
print('Existem {} pessoas maior de 21 anos de idade.'.format(velho))
print('Exitem {} pessoas menor de 21 anos de idade.'.format(novo))