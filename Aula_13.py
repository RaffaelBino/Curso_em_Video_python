#n = int(input('Digite um número: '))
#for c in range(0, n + 1):
#  for c in range(0, n+1, 2):   #  de 2 em 2
#    print(c)
#print('Fim!')
#i = int(input('Digite de onde começa seu número: '))
#f = int(input('Digite que número ele deve terminar: '))
#p = int(input('Digite de quantos em quantos números ele deve ir: '))
#for c in range(i, f+1, p):
#    print(c)
s = 0
for i in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print('O sómatorio de todos os valores é igual a {}.'.format(s))