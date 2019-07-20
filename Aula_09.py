frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print("""Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, 
Análise com len(), count(), find(), 
transformações com replace(), upper(), lower(), 
capitalize(), title(), strip(), junção com join().""")
print(frase.count('o'))  # Diferente de maiusculo
print(frase.upper().count('O'))  # Diferente de minusculo
print(len(frase))
frase1 = '   Curso em Vídeo Python   '
print(len(frase1))
print(len(frase1.strip()))
print(frase.replace('Python', 'Android'))
# frase = frase.replace('Curso', 'Aula')
print(frase)
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.lower().find('vídeo'))
print(frase.split())
