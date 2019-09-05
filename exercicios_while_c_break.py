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
