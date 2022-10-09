n1 = float(input('Qual foi sua nota no primeiro trimestre?'))
n2 = float(input('Qual foi sua nota no segundo trimestre?'))
n3 = float(input('Qual foi sua nota no terceiro trimestre?'))
n4 = float(input('Qual foi sua nota no quarto trimestre?'))
m = (n1+n2+n3+n4)/4
if m >= 6:
    print('Sua Media foi {:.2f} e você foi aprovado!'.format(m))
else:
    print('Sua Media foi {:.2f} e você foi reprovado!'.format(m))
print('Tenha um bom fim de ano!')
