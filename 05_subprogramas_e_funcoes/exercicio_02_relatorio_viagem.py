"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
distancia_km = float(input("qual a distancia em km:"))
consumo_kml = float(input("qual o consumo em kml:"))
preco_combustivel = float(input("qual o preço do combustivel:"))
def calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel):
    return distancia_km * consumo_kml * preco_combustivel
resposta1=calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)

def calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao):
    return qtd_pessoas * dias * diaria_alimentacao
qtd_pessoas=float(input("são quantas pessoas:"))
dias=float(input("são quantos dias:"))
diaria_alimentacao=float(input("qual a diaria de alimentação:"))
resposta2 = calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)
print("o custo da alimentação na viagem é de :",resposta2)
print("o custode transporte na viagem é de :",resposta1)
print("o custo total da viagem:",resposta1+resposta2)