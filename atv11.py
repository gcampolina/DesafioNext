def calcular_valor_venda(preco_custo, percentual_acrescimo):
    return preco_custo * (1 + percentual_acrescimo / 100)

preco_custo = float(input("Digite o preço de custo do produto: R$ "))
percentual_acrescimo = float(input("Digite o percentual de acréscimo (%): "))

valor_venda = calcular_valor_venda(preco_custo, percentual_acrescimo)


print("O valor de venda do produto é: R$", valor_venda)
