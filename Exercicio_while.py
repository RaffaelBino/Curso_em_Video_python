from random import randint
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
n = int(input('Qual o seu palpite? '))
while n != pc:
    print('Você errou!')
    n = int(input('Tente novamente: '))
print('Parabéns, eu pensei no número {} e você acertou !!'.format(pc))
