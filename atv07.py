def contar_vogais(string):
    vogais = set('aeiouAEIOU')
    contador_vogais = 0
    
   
    for caractere in string:
        if caractere in vogais:
            contador_vogais += 1
    
    return contador_vogais


string = input("Digite uma string: ")

numero_vogais = contar_vogais(string)
print(f"O número de vogais na string é: {numero_vogais}")
