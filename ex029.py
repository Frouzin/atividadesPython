kmh = int(input('Qual é a sua velocidade?'))
multa = (kmh-80)*7
if kmh > 80:
    print('Você esta muito rapido e será multado em {}'.format(multa))
else:
    print('Você está numa velocidade normal, pode seguir viagem!')
