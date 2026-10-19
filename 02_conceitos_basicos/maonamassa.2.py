# nome_produto = "celular"
# quantidade_estoque = 50
# preco_unitario = 800.0
# disponivel_para_venda = True

# print("bem-vindo a nossa empresa ")
# quanto = input("a empresa ta com que11ima de estoque com otimas ofertas.Você deseja quantos celulares?") 
# valordacompra = int(quanto) * float(preco_unitario)
# print(f"o valor da compra deu {valordacompra:.2f} deseja continuar? ")

#  TODO: Desenvolva seu algoritmo aqui
# 1. Leia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pessoa
# 4. Imprima formatado usando f-string

from re import L


print("bem-vindo ao programa que divide o valor de sua compra entre todos os entegrantes ")
bom = float(input("digite o valor  da conta:"))
pessoas = int(input("digite o numero de pessoas:"))
resutado = float(bom)/ int(pessoas)
print(f"ficara {resutado:.2f} para cada entegrante ")
