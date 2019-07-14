# Operações Aritiméticas
n1 = 5
n2 = 2
print(n1 + n2)  # Soma
print('Valor da soma é {}'.format(n1+n2))  # Soma

print(n1 - n2)  # Subtração
print('Valor da subtração é {}'.format(n1-n2))  # Subtração

print(n1 * n2)  # Multiplicação
print('Valor da multiplicação é {}'.format(n1*n2))  # Multiplicação

print(n1 / n2)  # Divisão
print('Valor da divisão é {}'.format(n1/n2))  # Divisão
print('Valor da divisão é {:.3f}'.format(n1/n2))  # Divisão com formatação de números

print(n1 ** n2)  # Potência
print('Valor da potência é {}'.format(n1*n2))  # Potência

print(n1 // n2)  # Divisão Inteira
print('Valor da divisão inteira é {}'.format(n1//n2))  # Divisão Inteira

print(n1 % n2)  # Resto da Divisão
print('Valor do resto da divisão é {}'.format(n1%n2))  # Resto da Divisão

print('O valor da soma é {}, o valor da multiplicação é {} e o valor da divisão inteira é {}'.format(n1+n2, n1*n2, n1//n2), end=' ')
print('e o valor do resto da divisão é {}.'.format(n1%n2))

print('='*30)

# Formatação com Strings

nome = input('Digite seu nome: ')
print('Olá {:~^10}, prazer em te conhecer!'.format(nome))  # Preenche com o simbulo os espaços faltantes
print('Olá {:>10}, prazer em te conhecer!'.format(nome))  # Coloca para a direita
print('Olá {:<10}, prazer em te conhecer!'.format(nome))  # Coloca para a esquerda
print('Olá {:^10}, prazer em te conhecer!'.format(nome))  # Centraliza
