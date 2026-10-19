"""
EXERCÍCIO 05: Acesso à Bilheteria do Parque
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba a idade do visitante (valor base do ingresso: R$ 100,00):
- Menor que 12 anos: "Infantil" (50% de desconto -> R$ 50,00)
- Maior ou igual a 60 anos: "Melhor Idade" (Gratuidade -> R$ 0,00)
- Demais idades: "Integral" (R$ 100,00)

Imprima o tipo de bilhete e o valor final a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
print("cinema")
print("estamos com promossoes com base em sua idade")
print("valor base do ingresso: R$ 100,00")
print("Menor que 12 anos: Infantil (50% de desconto -> R$ 50,00)")
print("Maior ou igual a 60 anos: Melhor Idade (Gratuidade -> R$ 0,00)")
print("Demais idades: Integral (R$ 100,00)")
idade = int(input("qual sua idade?"))
if idade >=60:
    print("Melhor Idade (Gratuidade -> R$ 0,00)")
elif idade <=12 :
    print("50% de desconto -> R$ 50,00")
else:
    print("o valor que ira paga sera Integral (R$ 100,00)")
