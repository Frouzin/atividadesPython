import random
nh = int(input('Digite um numero de 1 a 5:'))
nc = random.randint(1, 5)
print('Numero do PC', nc)
if nh == nc:
    print('Seu numero foi {} e o do computador foi {} ! Parabéns você venceu!'.format(nh, nc))
else:
    print('seu numero foi {} e o do computador foi {}, infelizmente você perdeu.'.format(nh, nc))
print('Obrigado por jogar!')
