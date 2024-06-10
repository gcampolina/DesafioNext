def calcular_total_a_pagar(quantidade, preco_unitario):
    total = quantidade * preco_unitario
    
    
    if quantidade <= 5:
        desconto = 0.02
    elif 5 < quantidade <= 10:
        desconto = 0.03
    else:
        desconto = 0.05

    
    valor_desconto = total * desconto
    total_a_pagar = total - valor_desconto
    
    return total, valor_desconto, total_a_pagar


descricao_produto = input("Digite a descrição do produto: ")
quantidade_adquirida = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário: "))


total, valor_desconto, total_a_pagar = calcular_total_a_pagar(quantidade_adquirida, preco_unitario)


print(f"Descrição do produto: {descricao_produto}")
print(f"Quantidade adquirida: {quantidade_adquirida}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Total: R$ {total:.2f}")
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")
