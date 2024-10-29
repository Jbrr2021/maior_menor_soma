maior = 0
menor = 9999
soma = 0

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número: "))
    maior = max(maior, numero)
    menor = min(menor, numero)
    soma += numero

media = soma / 10

print("O maior número é:", maior)
print("O menor número é:", menor)
print("A média dos números é:", media)