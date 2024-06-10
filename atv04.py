def processar_numeros(numeros):
    multiplicacao_pares = 1
    soma_impares = 0
    
    for numero in numeros:
        if numero % 2 == 0:
            multiplicacao_pares *= numero
        else:
            soma_impares += numero
    
    return multiplicacao_pares, soma_impares

def ler_numero_inteiro(prompt):
    while True:
        try:
            numero = int(input(prompt))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

numeros = []
for i in range(10):
    numero = ler_numero_inteiro(f"Digite o número {i+1}: ")
    numeros.append(numero)


multiplicacao_pares, soma_impares = processar_numeros(numeros)


print(f"Multiplicação dos números pares: {multiplicacao_pares}")
print(f"Soma dos números ímpares: {soma_impares}")
