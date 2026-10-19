"""
EXERCÍCIO 02: Consumo da Kawasaki Versys 300
Disciplina: Lógica de Programação com Python

ENUNCIADO:#
Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
solicite:
1. A distância total percorrida (em Km).
2. O total de combustível gasto (em Litros).

Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
from sys import float_info

print ("bem-vindo a nossa empresa")
ditancia = input("qual a distância total percorrida?")
cumbustivel = input("qual o total de combustível gasto?")
resultado1 = int(ditancia)+int(cumbustivel)
resultado2 = (resultado1)/2
print (f"{resultado2:.2f} litros por quilometro")