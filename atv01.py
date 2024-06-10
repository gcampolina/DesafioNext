def calcular_media(nota1, nota2, nota3, nota4):
    return (nota1 + nota2 + nota3 + nota4) / 4

while True:
    print("Digite as notas bimestrais:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))
    
    media = calcular_media(nota1, nota2, nota3, nota4)
    print(f"A média das notas é: {media:.2f}")
    
    continuar = input("Deseja continuar (S/N)? ").strip().upper()
    if continuar == 'N':
        break

print("Programa encerrado.")
