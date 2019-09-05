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
