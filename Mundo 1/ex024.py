cidade = str(input('Digite o nome de uma cidade:')).strip()
# print("Me de o numero 0 se tem Santo no Começo:", cidade.find('Santo'))
print(cidade[:5].upper() == "SANTO")
