"""
Ler um conjunto de números reais, armzenando-o em vetor e calcular o quadrado das componentes deste vetor,
armazenando o resultado em outro vetor.

Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.
"""

conjunto = []
for n in range(1, 11):
    numeros = int(input(f'Digite o {n}º número: '))
    conjunto.append(numeros)

quadrado = [n * n for n in conjunto]  # list comprehension

print(conjunto)
print(quadrado)

