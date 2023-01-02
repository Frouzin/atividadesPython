d = int(input('Por quantos dias o cliente alugou o carro? '))
kmr = float(input('Quantos KMs foram rodados no carro? '))
Paga = (d*60)+(kmr*0.15)
print('Se o Cliente Rodou por {} dias e {:.2f}KM, ele deverá pagar R${:.2f}'.format(d, kmr, Paga))
