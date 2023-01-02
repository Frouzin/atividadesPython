d = float(input('Digite o Salario do Funcionario: R$'))
p = int(input('Informe quantos % você dará de reajuste: '))
aumento = d+(d*(p/100))
print('Com o aumento o Salário que era de R${},com {}% de reajuste, passará a ser R${:.2f}'.format(d, p, aumento))
