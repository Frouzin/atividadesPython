km = int(input('Quantos é a distancia da sua viagem em KM? '))
ck = km*0.5
ckm = km*0.45
if km <= 200:
    print('Você irá percorrer {}KM e terá que pagar R${:.2f}'.format(km, ck))
else:
    print('Você irá percorrer {}KM e terá que pagar R${:.2f}'.format(km, ckm))
print('---Boa Viagem---')
