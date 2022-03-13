n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))

maior = menor = 0

if n1 > n2 and n1 >n3:
    maior = n1 
elif n2 > n1 and n2 > n3:
    maior = n2 
else:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1 
elif n2 < n1 and n2 < n3:
    menor = n2 
else:
    menor = n3
print(f'O maior número é {maior} e o menor é {menor}')