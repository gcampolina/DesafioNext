def calcular_mencao(media):
    if media >= 7:
        return "Aprovado"
    elif media <= 5:
        return "Reprovado"
    else:
        return "Recuperação"

nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

mencao = calcular_mencao(media)

print("Nome do aluno:", nome_aluno)
print("Menção:", mencao)
