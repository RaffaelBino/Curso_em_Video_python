s = n = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#  print('A soma dos números é {}'.format(s))
print(f'A soma dos números é {s}')
