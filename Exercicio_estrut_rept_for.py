from time import sleep
# Exercicio 46
print('='*20, 'Primeiro exercicio','='*20)
for i in range(10, -1, -1):
    print(i)
    sleep(.5)
print('FELIZ ANO NOVO!!!')

# Exercicio 47
print('='*20, 'Segundo exercicio','='*20)
for i in range(0, 51):
    if i % 2 == 0:
        print(i, end=' ')
print('Acabou')
