"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
1 - Cachorro Quente: R$ 4.00
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
# print("bem-vindo ao nosso restaurante")
# print("nosso restaurante está com as seguintes ofertas")
# print("1 - Cachorro Quente: R$ 4.00")
# print("2 - X-Bacon: R$ 5.00")
# print("3 - Torrada Simples: R$ 2.00")
# print("4 - Refrigerante: R$ 1.50")

# compra1 = int(input("foram consumido quantos Cachorro Quente?"))
# if compra1<0:
#     print("Impossivel calcular")
# compra2 = int(input("foram consumido quantos X-Bacon?"))
# if compra2<0:
#     print("Impossivel calcular")
# compra3 = int(input("foram consumido quantas Torrada Simples?"))
# if compra3<0:
#     print("Impossivel calcular")
# compra4 = int(input("foram consumido quantos refrigerantes?"))
# if compra4<0:
#     print("Impossivel calcular")
# resultado1 = float(compra1*4)
# resultado2 = float(compra2*5)
# resultado3 = float(compra3*2)
# resultado4 = float(compra4*1.5)
# valor = float(resultado1+resultado2+resultado3+resultado4)
# print(f"total a pagar:R${valor:.2f}")

# 1 - Cachorro Quente: R$ 4.00
# 1 - Cachorro Quente: R$ 4.00
# 3 - X-Bacon: R$ 5.00
# 4 - Torrada Simples: R$ 2.00
# 5 - Refrigerante: R$ 1.50

coisa = int(input("digite o codigo do produto consumido"))
if coisa == 1:
    valor = int(input(" a quantidade consumida ?"))
    resutado = 4*valor
    print(f"valor a ser pago:R${resutado:.2f}")
elif coisa ==2:
    valor = int(input(" a quantidade consumida ?"))
    resutado = 4*valor
    print(f"valor a ser pago:R${resutado:.2f}")
elif coisa == 3:
    valor = int(input(" a quantidade consumida ?"))
    resutado = 5*valor
    print(f"valor a ser pago:R${resutado:.2f}")
elif coisa == 4:
    valor = int(input(" a quantidade consumida ?"))
    resutado =  float(valor)*1.5
    print(f"valor a ser pago:R${resutado:.2f}")
else :
    print("este produto não existe")