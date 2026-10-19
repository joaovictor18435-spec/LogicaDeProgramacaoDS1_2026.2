"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario = float(input("qual seu salario?"))
if (salario)<=400:
    resultade = (salario/100)*15
    resultado = salario+resultade
    print (f"o aumento de seu salario é de ({resultade:.2f})")
    print (f"o seu salario é de : {resultado:.2f} ")
    print ("percentual aplicado é de 15%")
elif (salario)<=800:
    resultade2 = (salario/100)*12
    resultado2 = salario+resultade2
    print (f"o aumento de seu salario é de ({resultade2:.2f})")
    print (f"o seu salario é de : {resultado2:.2f}")
    print ("percentual aplicado é de 12%")
elif (salario)<=1200:
    resultade3 = (salario/100)*10
    resultado3 = salario+resultade3
    print (f"o aumento de seu salario é de ({resultade3:.2f})")
    print (f"o seu salario é de : {resultado3:.2f}")
    print ("percentual aplicado é de 10%")
elif (salario)<=2000:
    resultade4 = (salario/100)*7
    resultado4 = salario+resultade4
    print (f"o aumento de seu salario é de ({resultade4:.2f})")
    print (f"o seu salario é de : {resultado4:.2f}")
    print ("percentual aplicado é de 7%")
else:
    resultade5 = (salario/100)*4
    resultado5 = salario+resultade5
    print (f"o aumento de seu salario é de ({resultade5:.2f})")
    print (f"o seu salario é de : {resultado5:.2f}")
    print ("percentual aplicado é de 5%")
