# Exercicio 57
print('=' * 20, 'Primeiro exercicio', '=' * 20)
sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]  # O [0] serve para pegar apenas a primeira letra do que for digitado
while sexo not in 'MmFf':
    sexo = str(input('Dados incorretos! Por favor digite M ou F: ')).upper().strip()
print('Sexo {} registrado com sucesso!'.format(sexo))

# Exercicio 58
print('=' * 20, 'Segundo exercicio', '=' * 20)
