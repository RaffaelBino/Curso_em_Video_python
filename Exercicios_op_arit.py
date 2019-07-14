# Desafio 10 da aula 7
from builtins import int

print('='*20, 'Primeiro exercicio', '='*20)
h = float(input('Digite a altura da sua parede: '))
l = float(input('Digite a largura da sua parede: '))
a = h * l
lt = a/2
print('')
print('Serão nescessários {:.3f} litros de tinta para pintar sua parede.'.format(lt))
print('')

# Exercicio 5
print('='*20, 'Segundo exercicio','='*20)
n = int(input('Digite um numero e eu direi qual é seu atencessor e o seu sucessor: '))
print('Seu atencessor é {}'.format(n-1))
print('Seu sucessor é {}'.format(n+1))

# Exercicio 6
print('='*20, 'Terceiro exercicio', '='*20)
n = int(input('Digite um número: '))
print('O dobro do seu número é {} '.format(n*2))
print('O triplo do seu número é {} '.format(n*3))
print('A raiz quadrada de {} é {:.2f} '.format(n, (n ** 0.5)))
print('')

# Exercicio 7
print('='*20, 'Quarto exercicio','='*20)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A média das notas {} e {} é igual a {:.1f}'.format(n1, n2, m))
print('')

# Exercicio 9
print('='*20, 'Quinto exercicio','='*20)
n = int(input('Digite um número para ver sua tábuada: '))
print('='*15)
print('{} x 1 = {}'.format(n, n*1))
print('{} x 2 = {}'.format(n, n*2))
print('{} x 3 = {}'.format(n, n*3))
print('{} x 4 = {}'.format(n, n*4))
print('{} x 5 = {}'.format(n, n*5))
print('{} x 6 = {}'.format(n, n*6))
print('{} x 7 = {}'.format(n, n*7))
print('{} x 8 = {}'.format(n, n*8))
print('{} x 9 = {}'.format(n, n*9))
print('{} x 10 = {}'.format(n, n*10))
print('='*15)

# Exercicio 10
print('='*20, 'Sexto exercicio','='*20)
n = float(input('Quantos reais você tem na carteira ? : '))
d = n/3.74
print('Com R${:.2f} você pode comprar U${:.2f}.'.format(n, d))

# Exercicio 12
print('='*20, 'Sétimo exercicio','='*20)
n = float(input('Digite o valor do produto: R$'))
d = 5
vf = n - (n * (d / 100))
print('O produto que valia R${:.2f}, com 5% de desconto está valedo R${:.2f}.'.format(n, vf))

# Exercicio 13
print('='*20, 'Oitavo exercicio','='*20)
n = float(input('Qual o salário do funcionário: '))
d = 15
vf = n + (n * (d / 100))
print('O salário de RS{:.2f} desse funcionario, com o aumento ficou em R${:.2f}'.format(n, vf))

# Exercicio 14
print('='*20, 'Nono exercicio','='*20)
c = float(input('Digite a temperatura em °C : '))
f = c * (9/5) + 32
print('Em Celsius sua temperatura é {:.1f}°C e em Fahrenheit é {:.1f}°F'.format(c, f))

# Exercicio 14
print('='*20, 'Décimo exercicio','='*20)
nd = int(input('Quantos dias alugados ? '))
k = float(input('Quantos km rodados ? '))
vt = nd * 60
vk = k * 0.15
print('Total a pagar é R${:.2f}'.format(vt+vk))
