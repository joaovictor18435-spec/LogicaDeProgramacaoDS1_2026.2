nome =input("qual é seu nome?")
nascimento =input('em que dia você nasceu?')
mes =input('em que mês nasceu?')
ano =input("em que ano nesceu?")
print(f"seu nome é {nome} com a data de nascimento {nascimento}/{mes}/{ano}")
idade =2026 - int(ano)
if int(idade) < 12:
    print("você é uma criança")
elif int(idade) < 18 :
    print("você é adolecente")
elif int(idade) < 60:
    print ("você é adulto, tem responsabilidades")
else :
    print("idoso, tá pra morrer") 
print (f"este ano você completa aniversario na data {nascimento}/{mes}/2026")



