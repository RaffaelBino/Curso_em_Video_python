# Exercicio 36
print('='*20, 'Primeiro exercicio','='*20)
vlc = float(input('Valor da casa: R$ '))
slc = float(input('Salário do comprador: R$ '))
anos = int(input('Anos de financiamento: '))
prestacao = vlc / (anos * 12)
min = slc * (30 / 100)
print('Para pagar a casa de R${:.2f}, em {} anos, a prestação será de R${:.2f}'.format(vlc, anos, prestacao))
if prestacao <= min:
    print('Emprestimo pode ser Concedido!')
else:
    print('Emprestimo negado!')

# Exercicio 37
print('='*20, 'Segundo exercicio','='*20)
num = int(input('Digite um número inteiro: '))
print(''' Escolha uma das opções abaixo
[1]  Converter meu número para Binário
[2]  Converter meu número para Octal
[3]  Converter meu número para Hexadecimal''')
escolha = int(input('Sua escolha: '))
if escolha == 1:
    converte = bin(num)[2:]
    print('Seu número convertido para binário é: {}'.format(converte))
elif escolha == 2:
    converte = oct(num)[2:]
    print('Seu número convertido para Octal é: {}'.format(converte))
else:
    converte = hex(num)[2:]
    print('Seu número convertido para Hexadecimal é: {}'.format(converte))