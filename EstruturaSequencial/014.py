peso = int(input('Quantos KG de peixes você pescou? '))
excesso = peso - 50
multa = excesso * 4

print(f'Você pescou {peso}kg de peixes, passou {excesso}kg do limite de 50kg, deverá pagar R${multa:.2f}')
