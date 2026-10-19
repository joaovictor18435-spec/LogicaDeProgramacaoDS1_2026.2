"""
EXERCÍCIO 04: Casting de Dados e Idade em 2026
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba do usuário o ano de nascimento como texto (str).
Converta essa entrada para inteiro (int) utilizando o conceito de casting
e calcule a idade que a pessoa completará até o final de 2026.
Imprima a idade calculada com uma mensagem personalizada.
"""

# TODO: Desenvolva o algoritmo abaixo:
# Resposta 01

# nascimento = str(input("em que ano vacê nasceu?"))
# resposta = int(nascimento)
# calculo = 2026-int(resposta)
# print(f"você tera {calculo} ate o fim deste ano")

# resposta 02

nascimento =input("em que dia você nasceu?")
mes =input("em que mês nasceu?")
ano =input("em que ano nesceu?")
print(f"voce tem a data de nascimento {nascimento}/{mes}/{ano}")
idade =2026 - int(ano)
if int(idade) < 12:
    print("você é uma criança")
elif int(idade) < 18 :
    print("você é adolecente")
elif int(idade) < 60:
    print ("você é adulto, tem responsabilidades")
else :
    print("idosi, tá pra morrer") 
print (f"este ano você completa aniversario na data {nascimento}/{mes}/2026 e tera {idade} anos de idade")


