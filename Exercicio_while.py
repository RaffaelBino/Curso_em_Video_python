# Exercicio 57
print('=' * 20, 'Primeiro exercicio', '=' * 20)
sexo = str(input('Digite seu sexo: [M/F] ')).upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados incorretos! Por favor digite M ou F: ')).upper()
print('Sexo {} registrado com sucesso!'.format(sexo))
