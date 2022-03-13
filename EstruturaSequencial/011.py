num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))
num3 = float(input('Informe o terceiro numero: '))

prod = (num1 * 2) + (num2 / 2) 
soma = num1 * 3 + num3
terc = num3 ** 3

print(f'O produto do dobro do primeiro com a metade do segundo é {prod}')
print(f'A somado triplo do primeiro com oterceiro é {soma}')
print(f'O terceiro elevado ao cubo é {terc:.1f}')