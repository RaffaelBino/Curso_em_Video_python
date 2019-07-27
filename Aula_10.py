# nome = str(input('Qual é o seu nome ? ')).strip()
# if nome == 'Raffael':
# print('Que nome bonito!')
# else:
#  print('Seu nome é tão normal')
#  print('Olá, {}, tenha um bom dia'.format(nome))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi de {:.1f}')
if m >= 6:
    print('Parabéns! Você foi aprovado!')
else:
    print('Você ficou de recuperação')
#  print('Parabéns' if m >= 6 else 'Estude mais')
