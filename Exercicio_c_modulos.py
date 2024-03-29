import math, random, pygame

# Exercicio 16
print('=' * 20, 'Primeiro exercicio', '=' * 20)
n = float(input('Digite um numero: '))
# print('O numero digitado foi {} e a porção inteira dele é {}.'.format(n, math.floor(n)))   # Arredonda pra baixo
print('O numero digitado foi {} e a porção inteira dele é {}.'.format(n, math.trunc(n)))  # Quebra o número
print('')

# Exercicio 17
print('=' * 20, 'Segundo exercicio', '=' * 20)
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
# hp = (co**2 + ca**2) ** 0.5
hp = math.hypot(co, ca)
print('A hipotenusa desse triangulo retangulo mede {:.2f}'.format(hp))

# Exercicio 18
print('=' * 20, 'Terceiro exercicio', '=' * 20)
n = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {} tem o SENO de {:.2f}'.format(n, math.sin(math.radians(n))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(n, math.cos(math.radians(n))))
print('O ângulo de {} tem o TAGENTE de {:.2f}'.format(n, math.tan(math.radians(n))))

# Exercicio 19
print('=' * 20, 'Quarto exercicio', '=' * 20)
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
escohido = random.choice(lista)
print('O aluno(a) escolhido foi : {}'.format(escohido))

# Exercicio 20
print('=' * 20, 'Quinto exercicio', '=' * 20)
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)

# Exercicio 21  #Rodar musica
print('=' * 20, 'Sexto exercicio', '=' * 20)
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

