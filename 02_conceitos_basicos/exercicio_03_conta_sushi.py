"""
EXERCÍCIO 03: Conta do Nagoya Sushi House
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie um programa que:
1. Leia o valor total consumido no restaurante (em R$).
2. Aplique a taxa de 10% de serviço do garçom.
3. Exiba o valor final da conta a pagar com mensagem formatada.
"""

# TODO: Desenvolva o algoritmo abaixo:
print ("bem-vindo a nossa empresa")
consumo = input("qual o valor total consumido no restaurante?")
resutado1 = float(consumo)/100
resutado2 = float(resutado1)*10
resutado3 = float(resutado2)+float(consumo)
print (f"o valor da conta deu {resutado3:.2f}R$")

