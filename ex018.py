import math
# CO = float(input('Digite o tamanho do seu cateto oposto:'))
# CA = float(input('Digite o tamanho do seu cateto adjacente:'))
# HI = float(input('Digite o tamanho da sua hipotenusa:'))
# sen = CO/HI
# cos = CA/HI
# tan = CO/CA
# print('Dadas informações o seu seno é {:.2f}, o seu cosseno é {:.2f} e sua tangente é {:.2f}'.format(sen, cos, tan))
an = float (input('Digite o seu angulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('Dadas informações o seu seno é {:.2f}, o seu cosseno é {:.2f} e sua tangente é {:.2f}'.format(sen, cos, tan))
