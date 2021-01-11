"""
Faça um programa que leia um vetor de 8 posiçoes e, em seguida, leia também dois valores x e y quaisquer
correspondentes a duas posições do vetor.

Ao final, seu programa deverá escrever a soma dos valoçres encontrados nas respectivas posições x e y.
"""

lista = []

for pos in range(1, 8 + 1):
    num = int(input(f'Digite um númeor para a {pos}º posição: '))
    lista.append(num)

print('-' * 40)

while True:
    x = int(input('Escolha a primeira posição (entre 0 e 7): '))
    y = int(input('Escolha a segunda posição (entre 0 e 7): '))
    if x == y:
        print('-' * 40)
        print('Digite valores diferentes para primeira e segunda posições!')
    elif x < 0 or x > 7:
        print('-' * 40)
        print('Escolha valores entre 0 e 7!')
    elif y < 0 or y > 7:
        print('-' * 40)
        print('Escolha valores entre 0 e 7!')
    else:
        soma = lista[x] + lista[y]
        break

print('-' * 40)
print(f'Os valores são: {lista}')
print(f'A soma entre a primeira e a segunda posição escolhidas é: {soma}')

