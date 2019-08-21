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

