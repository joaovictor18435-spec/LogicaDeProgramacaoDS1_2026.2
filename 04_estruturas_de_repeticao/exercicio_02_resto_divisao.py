"""
EXERCÍCIO 02: Resto da Divisão por 5
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia dois valores inteiros X e Y.
Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)
cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

# TODO: Desenvolva o algoritmo abaixo:
# Leitura dos dois valores inteiros
X = int(input())
# Se os valores forem inseridos na mesma linha, use: X, Y = map(int, input().split())
Y = int(input())

# Determina o menor e o maior valor para garantir a ordem crescente
menor = min(X, Y)
maior = max(X, Y)

# Laço for para percorrer os números entre o menor e o maior (exclusivo)
for i in range(menor + 1, maior):
    # Verifica se o resto da divisão por 5 é igual a 2 ou 3
    if i % 5 == 2 or i % 5 == 3:
        print(i)