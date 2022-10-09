# num = str(input('Digite um numero de 0 até 9999: '))
# print('Unidade:', num[3:])
# print('Dezena:', num[2:3])
# print('Centena:', num[1:2])
# print('Milhar:', num[0:1])
num = int(input('Digite um numero de 0 até 9999: '))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar:{}'.format(m))