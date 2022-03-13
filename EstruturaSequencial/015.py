hor = float(input('Quanto você ganha por hora? '))
mhor = int(input('Quantas horas você trabalhou no mês? '))

sal = hor * mhor

ir =  sal * (11/100)
inss = sal * (8/100)
sindicato = sal * (5/100)

salliqui = sal - (ir + inss + sindicato)

print(f'''
Salário bruto R${sal:.2f}
Imposto de Renda R${inss:.2f}
INSS R${sindicato:.2f}
Salario liquido R${salliqui:.2f}
''')