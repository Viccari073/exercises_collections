"""
Crie um programa que lê 6 valçores inteiros e, em seguida, mostre na tela os valçores lidos na ordem inversa.
"""

valores = list()

for valor in range(1, 7):
    v = int(input(f'Digite o {valor}º valor: '))
    valores.append(v)

print(f'Os valores digitados, em ordem reversa são: {valores[::-1]}')
