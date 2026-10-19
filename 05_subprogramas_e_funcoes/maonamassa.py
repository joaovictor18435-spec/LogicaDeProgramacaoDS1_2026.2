# TODO: Defina a função calcular_media e teste-a abaixo
nota1=float(input("digite a primeira nota:"))
nota2=float(input("digite a segunda nota:"))
nota3=float(input("digite a teceira nota:"))

def calcular_media(nota1, nota2, nota3):
    return (nota1+nota2+nota3)/3

calculo1=calcular_media(nota1, nota2, nota3)
print(f"a media é: {calculo1}")