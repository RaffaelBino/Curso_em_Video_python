# escape sequence ANSI
print('\033[31mOlá, Mundo')
print('\033[30;43mOlá, Mundo')
print('\033[1;31;43mOlá, Mundo\033[m')
print('\033[4;31;43mOlá, Mundo\033[m')
print('\033[4;30;45mOlá, Mundo\033[m')

a = 1
b = 2
print('A soma é : \033[32m{}\033[m + \033[31m{}\033[m = \033[36m 3 \033[m'.format(a, b))

nome = 'Raffael'
print('Olá , prazer em revelo, {}{}{}'.format('\033[4;34m', nome, '\033[m'))