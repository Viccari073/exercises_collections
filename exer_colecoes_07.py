"""
Escreva um programa que leia 10 números inteiros e os armazene em um vetor.

Imprima o vetor, o maior elemento e a posição que ele se encontra.
"""

vetor = list()

for p in range(1, 11):
    valor = int(input(f'Digite o {p}º valor:'))
    vetor.append(valor)

print(vetor)
print(f'O maior valor é o {max(vetor)} na posição {vetor.index(max(vetor))}')
