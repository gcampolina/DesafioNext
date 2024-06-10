def calcular_custo_consumidor(custo_fabrica):
    impostos = custo_fabrica * 0.45
    custo_intermediario = custo_fabrica + impostos
    
    percentagem_distribuidor = custo_intermediario * 0.28
    
    custo_consumidor = custo_intermediario + percentagem_distribuidor
    
    return custo_consumidor


custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))


custo_consumidor = calcular_custo_consumidor(custo_fabrica)


print("O custo ao consumidor do carro é: R$", custo_consumidor)
