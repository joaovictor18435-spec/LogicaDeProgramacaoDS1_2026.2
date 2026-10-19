"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
print ("f(x)=Ax²+BX+C")
valordea = float(input ("determine um valor para A:"))
if (valordea)<=0:
    print("Impossivel calcular")
valordeb = float(input ("determine um valor para B:"))
valordec = float(input ("determine um valor para C:"))
resposta = ((valordeb)*(valordeb))+((-4)*(valordea)*(valordec))
if (resposta)<0:
    print("Impossivel calcular")
resposta1 = (resposta)**(1/2)
resposta2 = (((-(valordeb))+(resposta1))/(2*(valordea)))
resposta3 = (((-(valordeb))-(resposta1))/(2*(valordea)))
print(f"o resultado da equação do sengundo gral é:X¹={resposta2:.5F} ;X²={resposta3:.5F}  ")