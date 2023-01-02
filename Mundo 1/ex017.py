import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hq = math.pow(co,2)+math.pow(ca,2)
h = math.sqrt(hq)
print('O Comprimento da Hipotenusa é {:.2f}'.format(h))
