"""
EXERCÍCIO 01: Gestão de Tráfego Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
A loja Casas Paulino está veiculando anúncios no Meta Ads em Tianguá.
Escreva um programa que leia:
1. O valor total investido na campanha (em R$).
2. O número total de cliques obtidos.

Calcule e mostre na tela o Custo Por Clique (CPC) médio da campanha formatado em reais.
"""

# TODO: Desenvolva o algoritmo abaixo:

print ("bem-vindo a nossa empresa")
capital = input("qual o valor investido na campanha?")
cliques = input("digite O número total de cliques obtidos?")
resultado = float(capital)/int(cliques)
print(f"{resultado:.2f} R$ por clique")
