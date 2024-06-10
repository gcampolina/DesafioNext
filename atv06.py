def ler_lista_numeros():
    numeros = input("Digite uma lista de números separados por espaço: ")

    lista_numeros = [int(num) for num in numeros.split()]
    return lista_numeros


def ordenar_lista(lista_numeros):
    return sorted(lista_numeros)


lista_numeros = ler_lista_numeros()


lista_ordenada = ordenar_lista(lista_numeros)


print("Lista ordenada em ordem crescente:", lista_ordenada)
