download = float(input('Informe o tamanho do arquivo em MB: '))
mb = float(input('Informe a velocidade em Mbps: '))
mb1 = mb * 0.125
tempo = download / mb1

print(f'{tempo:.1f} segundos')