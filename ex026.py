f = str(input('Digite uma frase: ')).lower().strip()
print('Quantas vezes a letra "a" aparece:{}'.format(f.count('a')))
print('Qual é a primeira vez que aparece a letra "a":', f.find('a')+1)
print('Qual é a ultima vez que a aparece a letra "a":', f.rfind('a')+1)
