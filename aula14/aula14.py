import os
os.system("cls") # limpar a tela

carros = []
carro = input("Digite o nome do novo carro: ")
tam = len(carros)

while carro != "-1":
    carros.append(carro)
    carro = input("Digite o nome do novo carro: ")

os.system("cls")
for x in carros:
    print(x)

print("\nFim do programa.")
