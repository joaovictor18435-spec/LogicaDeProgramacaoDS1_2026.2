"""
EXERCÍCIO 01: Imposto de Renda de Lisarb
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de uma pessoa em Rombus (R$).
- Até R$ 2000.00: Isento
- De R$ 2000.01 até R$ 3000.00: 8% sobre o excedente de R$ 2000.00
- De R$ 3000.01 até R$ 4500.00: 18% sobre o excedente de R$ 3000.00 + 8% da faixa anterior
- Acima de R$ 4500.00: 28% sobre o que ultrapassar R$ 4500.00 + impostos anteriores

Imprima "Isento" ou o valor total do imposto formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario = float(input("qual seu salário?"))
if float(salario) <= 2000:
    print("Isento")
elif float(salario) <=3000.00:
    resultado = ((salario)-(2000))*0.08
    print(f"seu imposto sera de :{resultado:.2f}")
elif float(salario) <=4500:
    resultado2 = ((salario-3000)/100*18)+(((salario)-(2000))/100 *8)
    print(f"seu imposto sera de :{resultado2:.2f}")
else :
    resultado3 = ((salario-4500)/100 * 28)+((salario-3000)/100*18)+(((salario)-(2000))/100 *8)
    print(f"seu imposto sera de :{resultado3:.2f}")
