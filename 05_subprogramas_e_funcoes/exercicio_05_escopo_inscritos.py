"""
EXERCÍCIO 05: Gestão de Escopo Global e Local
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Declare a variável global total_inscritos = 0.
Crie a função `inscrever_aluno(quantidade)` utilizando a diretiva `global`
para atualizar a variável. Demonstre o valor de total_inscritos antes e depois da chamada.
"""

# TODO: Desenvolva o algoritmo abaixo:
total_inscritos = 0
while True:
    aluno = str(input("você quer participar;"))
    if aluno=="sim":
        inscrever_aluno=1
        total_inscritos+=inscrever_aluno
    else:
        print("se increve aí:")
    if total_inscritos == 21:
        print("limite de incritos")
    break
print("total inscrito:",total_inscritos)

# total_inscritos = 0
