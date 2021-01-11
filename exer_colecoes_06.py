"""
Faça um programa que receba do usuário um vetor com 10 posiçãoes. Em seguida, deverá ser impresso
o maior e o menor elemento de cada vetor.
"""

vetor = list()

for p in range(1, 11):
    valor = int(input(f'Digite um valor para a {p}ª posição: '))
    vetor.append(valor)

print(f'O maior valor é: {max(vetor)}')
print(f'O menor valor é: {min(vetor)}')
