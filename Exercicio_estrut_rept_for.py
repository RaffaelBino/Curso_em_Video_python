

# Exercicio 56
print('=' * 20, 'Décimo primeiro exercicio', '=' * 20)
somaidade = 0
qtdnova = 0
for i in range(1, 5):
    print('{}° pessoa'.format(i))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: '))
    somaidade += idade
    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    elif sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        qtdnova += 1

mediaidade = somaidade / 4
print('A média da idade das pessoas é {:.1f}.'.format(mediaidade))
print('O homem mais velho tem {} e se chama {}.'.format(maioridadehomem, nomevelho))
print('No grupo tem {} mulheres abaixo de 20 anos'.format(qtdnova))
