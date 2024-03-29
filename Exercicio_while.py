from random import randint
from time import sleep
from math import factorial
# Exercicio 57
print('=' * 20, 'Primeiro exercicio', '=' * 20)
sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]  # O [0] serve para pegar apenas a primeira letra do que for digitado
while sexo not in 'MmFf':
    sexo = str(input('Dados incorretos! Por favor digite M ou F: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))

# Exercicio 58
print('=' * 20, 'Segundo exercicio', '=' * 20)
print('Olá sou seu computador...')
pc = randint(1, 10)
print('Acabei de advinhar um número de 0 a 10')
print('Será que você consegue advinhar? ')
tentativa = 1
n = int(input('Qual o seu palpite? '))
while n != pc:
    if n < pc:
        print('Mais...', end=' ')
    elif n > pc:
        print('Menos...', end=' ')
    n = int(input('Tente novamente: '))
    tentativa += 1
print('Parabéns, eu pensei no número {} e você acertou em {} tentativas !!'.format(pc, tentativa))

# Exercicio 59
print('=' * 20, 'Terceiro exercicio', '=' * 20)
x = int(input('Digite o 1° número: '))
y = int(input('Digite o 2° número: '))
z = 0
while z == 0:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')
    opcao = int(input('Qual é a sua opção ? '))
    if opcao == 1:
        print('A soma de {} + {} = {}.'.format(x, y, x + y))
    elif opcao == 2:
        print('A multiplicação de {} x {} = {}.'.format(x, y, x * y))
    elif opcao == 3:
        if x > y:
            print('o número {} é maior que o número {}.'.format(x, y))
        else:
            print('o número {} é maior que o número {}.'.format(y, x))
    elif opcao == 4:
        x = int(input('Digite o 1° número: '))
        y = int(input('Digite o 2° número: '))
    elif opcao == 5:
        z += 1
        print('Programa Finalizando!')
        sleep(1)
    else:
        print('Digite um número válido')
print('Programa Finalizado!')

# Exercicio 60
print('=' * 20, 'Quarto exercicio', '=' * 20)
n = int(input('Digite um número para ver seu fatorial: '))
#f = factorial(n)
#print('O Fatorial de {} é {}.'.format(n, f))
c = n
f = 1
print('Calculando {}!'.format(n))
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

# Exercicio 61
print('=' * 20, 'Quinto exercicio', '=' * 20)
pm = int(input('Digite o primeiro termo da sua PA: '))
raz = int(input('Digite a razão da sua PA: '))
termo = pm
k10 = 1
while k10 <= 10:
    print('{} -> '.format(termo), end='')
    termo += raz
    k10 += 1
print('Fim')

# Exercicio 62
print('=' * 20, 'Sexto exercicio', '=' * 20)
pm = int(input('Digite o primeiro termo da sua PA: '))
raz = int(input('Digite a razão da sua PA: '))
termo = pm
k10 = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while k10 <= total:
        print('{} -> '.format(termo), end='')
        termo += raz
        k10 += 1
    print('Pausa')
    mais = int(input('Você quer mais quantos termos ? '))
print('FIM!!')
print('Foram mostrados {} termos ao final do programa.'.format(total))

# Exercicio 63
print('=' * 20, 'Sétimo exercicio', '=' * 20)
ns = int(input('Digite quantos números você deseja ver na sequência de Fibonacci: '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= ns:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM!')

# Exercicio 64
print('=' * 20, 'Oitavo exercicio', '=' * 20)
n = cont = total = 0
n = int(input('Digite um número: [999 para parar] '))
while n != 999:
    cont += 1
    total += n
    n = int(input('Digite um número: [999 para parar] '))
# print('Você digitou {} números e a soma deles é {}.'.format(cont - 1, total - 999))
print('Você digitou {} números e a soma deles é {}.'.format(cont, total))

# Exercicio 65
print('=' * 20, 'Nono exercicio', '=' * 20)
sn = 'S'
soma = tot = media = maior = menor = 0
while sn == 'S':
    n = int(input('Digite um número: '))
    soma += n
    tot += 1
    if tot == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    sn = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
media = soma / tot
print('A você digitou {} e sua média foi {:.2f} '.format(tot, media))
print('O maior número é o {} e o menor número é {}.'.format(maior, menor))