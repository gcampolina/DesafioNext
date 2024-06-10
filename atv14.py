def verificar_idade(idade):
    if idade >= 18:
        return "maior de idade"
    else:
        return "menor de idade"

for i in range(75):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    mensagem = verificar_idade(idade)
    print(f"A pessoa {i+1} é {mensagem}.")
