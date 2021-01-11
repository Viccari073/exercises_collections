"""
Leia um vetor de 10 posições. Contar e escrever quantos valores ele possui.
"""

from time import sleep

vetor = []
for p in range(1, 11):
    valor = int(input(f'Digite um valor para a {p}ª posição: '))
    vetor.append(valor)

for v in vetor:
    print(v)
    sleep(1)


print(vetor)
print(len(vetor))
