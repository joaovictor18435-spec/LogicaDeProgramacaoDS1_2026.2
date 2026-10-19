media_aluno = input("qual a media do aluno?")
frequencia_percentual = input("qual o percentual de frequencia?")
aprovado = float(media_aluno) >= 6 and float(frequencia_percentual)>=75
print("Status de aprovação:", aprovado)