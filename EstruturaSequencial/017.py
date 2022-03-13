area = float(input('Area a ser pintada '))
latas = area / 6
preco = (latas / 18) * 80
galoes = (latas / 3.6) * 25
print(f'''
Ao comprar apenas latas de 18 litros fica R${preco:.2f}
Ao comprar apenas galões de 3.6 litros fica R${galoes:.2f}
''')