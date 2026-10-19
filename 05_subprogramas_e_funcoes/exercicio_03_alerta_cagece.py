"""
EXERCÍCIO 03: Gerador de Alertas da Cagece
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Desenvolva um procedimento `emitir_alerta_fatura(nome_cliente, valor, data_vencimento)`
que imprima a mensagem:
"Prezado(a) [nome], sua fatura da Cagece no valor de R$ [valor] vence no dia [data]."
"""

# TODO: Desenvolva o procedimento abaixo:
def emitir_alerta_fatura(nome_cliente, valor, data_vencimento):
    print(f"Prezado(a) {nome_cliente}, sua fatura da Cagece no valor de R$ {valor} vence no dia {data_vencimento}")
nome_cliente = str(input("qual o nome do cliente:"))
valor= float(input("qual o valor a pagar:"))
data1=int(input("qual o dia do vencimento:"))
data2=int(input("qual o mes de vencimento:"))
data3=int(input("qual o ano de vencimento:"))
data_vencimento=print(f"{data1}/{data2}/{data3}")
resposta= emitir_alerta_fatura(nome_cliente, valor, data_vencimento)
# print(f"Prezado(a) {nome_cliente}, sua fatura da Cagece no valor de R$ {valor} vence no dia {data1}/{data2}/{data3}")
print(resposta)