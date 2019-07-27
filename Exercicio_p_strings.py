# Exercicio 22
print('='*20, 'Primeiro exercicio','='*20)
nome = str(input('Digite seu nome completo: ')).strip()
print('Análisando seu nome...')
print('Seu nome em maiusculo é: {}'.format(nome.upper()))
print('Seu nome em minusculo é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))

# Exercicio 23
print('='*20, 'Segundo exercicio','='*20)
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {} '.format(num))
print('Unidades: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhar: {}'.format(m))

# Exercicio 24
print('='*20, 'Terceiro exercicio','='*20)
cid = str(input('Em que cidade você nasceu? :')).strip()
print(cid[:5].upper() == 'SANTO')

# Exercicio 25
print('='*20, 'Quarto exercicio','='*20)
nome = str(input('Qual seu nome completo? ')).strip()
print('Seu nomoe tem Silva ? {}'.format('SILVA' in nome.upper()))

# Exercicio 26
print('='*20, 'Quinto exercicio','='*20)
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A apareceu {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))

# Exercicio 27
print('='*20, 'Sexto exercicio','='*20)
nome = str(input('Digite seu nome completo')).strip()
n = nome.split()
print('Seu primeiro nome é: {}'.format(n[0]))
print('Seu ultimo nome é: {}'.format(n[len(n)-1]))

