def palindromo(string):
    string = string.replace(" ", "").upper()

    return string == string[::-1]

string = input("Digite uma string: ")


if palindromo(string):
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
