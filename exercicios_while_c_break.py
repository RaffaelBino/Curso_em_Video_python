from random import randint
# Exercicio 66
print('=' * 20, 'Primeiro exercicio', '=' * 20)
s = c = 0
while True:
    n = int(input('Digite um número: (Digite 999 para parar )'))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foram {c} números e a soma deles é {s}')

# Exercicio 67
print('=' * 20, 'Segundo exercicio', '=' * 20)
while True:
    tabuada = int(input('Quer a tábuada de qual valor: '))
    if tabuada < 0:
        break
    for i in range(1, 11):
        print(f'{tabuada} x  {i} = {tabuada*i}')
print('Programa finalizado!')

# Exercicio 68
print('=' * 20, 'Terceiro exercicio', '=' * 20)
print('='*10)
print('Par ou Ímpar')
print('='*10)
ganhos = 0
while True:
    dedos = int(input('Digite um valor: '))
    pi = str(input("Par ou Ímpar: [P/I]")).upper().strip()[0]
    dedospc = randint(1, 10)
    somadedos = dedos + dedospc
    print('-' * 5)
    print(f'Você jogou {dedos} e o Computador jogou {dedospc}.', end='')
    if somadedos % 2 == 0 and pi == 'P':
        print(f'O total deu {somadedos}, que é PAR')
        print('Você GANHOU!!')
        ganhos += 1
        print('Vamos Jogar de novo')
    elif somadedos % 2 == 1 and pi == 'I':
        print(f'O total deu {somadedos}, que é ÍMPAR')
        print('Você GANHOU!!')
        ganhos += 1
        print('Vamos Jogar de novo')
    else:
        if pi == 'P':
            print(f'O total deu {somadedos}, que é ÍMPAR')
        elif pi == 'I':
            print(f'O total deu {somadedos}, que é PAR')
        print(' Você Perdeu!')
        break
print(f'Game Over!! Você ganhou {ganhos} vez(es)')

# Exercicio 69
print('=' * 20, 'Quarto exercicio', '=' * 20)
print('CADESTRE UMA PESSOA')
maioridade = homens = mulher20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]')).upper().split()[0]
    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulher20 += 1
    cont = str(input('Quer continuar? [S/N}')).upper().split()[0]
    if cont == 'N':
        break
print(f'O total de pessoas com mais de 18 anos: {maioridade}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com mais de 20 anos: {mulher20}')
