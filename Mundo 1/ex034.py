d = float(input('Digite o salario do funcionario:'))
ajuste = d+(d*(15/100))
ajuste1 = d+(d*(10/100))
if d > 1250:
    print('Quem recebe R${}, passará a receber R${}'.format(d, ajuste1))
else:
    print('Quem recebe R${}, passará a receber R${}'.format(d, ajuste))
