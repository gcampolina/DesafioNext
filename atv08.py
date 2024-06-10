def calcular_fatorial(numero):
    if numero < 0:
        return "Não é possível calcular o fatorial de um número negativo."
    fatorial = 1

    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial


def ler_numero_inteiro(prompt):
    while True:
        try:
            numero = int(input(prompt))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

numero = ler_numero_inteiro("Digite um número inteiro: ")
resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")
