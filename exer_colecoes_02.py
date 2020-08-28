"""
Crie um programa que lê 6 valores inteiros e, em seguida, mostre os valores lidos.
"""

lista_valores = list()

for n in range(1, 6 + 1):
    valor = int(input(f'Digite o {n}º valor: '))
    lista_valores.append(valor)

print(f'Os valores lidos foram: {lista_valores}')
