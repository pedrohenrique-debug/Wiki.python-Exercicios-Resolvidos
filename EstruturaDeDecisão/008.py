p1 = str(input('Nome produto 1: '))
p1p = float(input('Preço: '))

p2 = str(input('Nome produto 2: '))
p2p = float(input('Preço: '))

p3 = str(input('Nome produto 3: '))
p3p = float(input('Preço: '))
comprar = 0
if p1p < p2p and p1p < p3p:
    comprar = p1
elif p2p < p1p and p2p < p3p:
    comprar = p2
else: 
    comprar = p3

print(f'Compre {comprar}')