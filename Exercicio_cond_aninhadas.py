from datetime import date
from random import randint
from time import sleep

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
elif escolha == 3:
    converte = hex(num)[2:]
    print('Seu número convertido para Hexadecimal é: {}'.format(converte))
else:
    print('Opção Inválida! Tente Novamente.')

# Exercicio 38
print('='*20, 'Terceiro exercicio','='*20)
print('Digite dois números')
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('O primeiro Valor é maior')
elif n2 > n1:
    print('O segundo valor é maior')
else:
    print('Os valores são iguais')

# Exercicio 39
print('='*20, 'Quarto exercicio','='*20)
anoatual = date.today().year
nasc = int(input('Em que ano você nasceu ? '))
idade = anoatual - nasc
print('Quem nasceu em {}, tem {} anos no ano de {}.'.format(nasc, idade, anoatual))
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!!')
elif idade < 18:
    saldo = 18 - idade
    print('Faltam {} anos pro seu alistamento'.format(saldo))
    ano = anoatual + saldo
    print('Seu alistamento será em {}'.format(ano))
else:
    saldo = idade - 18
    print('Você ja deveria ter se alistado a {} anos'.format(saldo))
    ano = anoatual - saldo
    print('Seu a listamento foi em {}'.format(ano))

# Exercicio 40
print('='*20, 'Quinto exercicio','='*20)
nt1 = float(input('Digite a primeira nota: '))
nt2 = float(input('Digite a segunda nota: '))
m = (nt1 + nt2) / 2
if m < 5:
    print('Sua média foi {:.1f}.'.format(m))
    print('Você foi REPROVADO!')
elif m >= 7:
    print('Sua média foi {:.1f}.'.format(m))
    print('Você está APROVADO!')
else:
    print('Sua média foi {:.1f}.'.format(m))
    print('Você está de RECUPERAÇÃO')

# Exercicio 41
print('='*20, 'Sexto exercicio','='*20)
anonasc = int(input('Ano de nascimento: '))
anoatual = date.today().year
idades = anoatual - anonasc
print('O atléta tem {} anos.'.format(idades))
if idades <= 9:
    print('Classificação MIRIM')
elif idades <= 14:
    print('Classificação INFANTIL')
elif idades <= 19:
    print('Classificação JÚNIOR')
elif idades <= 25:
    print('Classificação SÊNIOR')
else:
    print('Classificação MASTER')

# Exercicio 42
print('='*20, 'Sétimo exercicio','='*20)
l1 = int(input('Digite o primeiro segmento: '))
l2 = int(input('Digite o segundo segmento: '))
l3 = int(input('Digite o terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os seguimentos acima PODEM formar um triangulo', end=' ')
    if l1 == l2 == l3:
        print('e será um trinângulo EQUILÁTERO')
    elif l1 != l2 != l3 != l1:
        print('e será um trinângulo ESCALENO')
    else:
        print('e será um trinângulo ISÓSCELES')
else:
    print('Os seguimentos acima NÃO PODEM formar um trinangulo')

# Exercicio 43
print('='*20, 'Oitavo exercicio','='*20)
peso = float(input('Qual é o seu pese? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso/(altura**2)
print('Seu imc deu: {:.1f} '.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('Você está com o PESO NORMAL!')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBSIDADE MORBIDA, procure um médico/nutricionista')

# Exercicio 44
print('='*20, 'Nono exercicio','='*20)
print('{:+^40}'.format(' Loja '))
preco = float(input('Preço das compras: R$'))
print(''' Formas de Pagamento
[ 1 ] À vista / Débito (10% de desconto)
[ 2 ] À vista (Cartão de crédito)/(5% de desconto)
[ 3 ] 2x no Cartão 
[ 4 ] 3x ou mais no cartão ( 20% de juros )''')
opcao = int(input('Escolha sua forma de pagamento: '))
if opcao == 1:
    print('O valor da(s) sua(s) compra(s) era R${:.2f} e ficou em: R${:.2f}'.format(preco, preco - (preco * (10/100))))
elif opcao == 2:
    print('O valor da(s) sua(s) compra(s) era R${:.2f} e ficou em: R${:.2f}'.format(preco, preco - (preco * (5 / 100))))
elif opcao == 3:
    print('O valor da(s) sua(s) compra(s) era R${:.2f} e ficou em: R${:.2f}'.format(preco, preco))
elif opcao == 4:
    totparc = int(input('Quantas parcelas ?'))
    juros = preco + (preco * 20/100)
    total = juros / totparc
    print('O valor da(s) sua(s) compra(s) era de R${:.2f}, após ser parcelada em: {}x, ficou em: R${:.2f}'.format(preco, totparc, juros))
    print('O Valor das suas parcelas serão: R${:.2f}'.format(total))
else:
    print('Digite uma Opção válida!')

# Exercicio 45
print('='*20, 'Decimo exercicio','='*20)
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print(''' Opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual a sua jogada ? '))
print('Pedra')
sleep(1)
print('Papel')
sleep(1)
print('Tesoura')
sleep(1)
print('~'*30)
print('Computador jogou {}.'.format(itens[pc]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('~'*30)
if jogador == pc:
    print('Empatou')
elif jogador == 0 and pc == 1:
    print('Computador ganhou!')
elif jogador == 1 and pc == 0:
    print('Jogador ganhou!')
elif jogador == 2 and pc == 0:
    print('Computador ganhou!')
elif jogador == 0 and pc == 2:
    print('Jogador ganhou!')
elif jogador == 1 and pc == 2:
    print('Computador ganhou!')
elif jogador == 2 and pc == 1:
    print('Jogador ganhou!')
else:
    print('Digite um número válido!!!')

