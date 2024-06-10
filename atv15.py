total_carros_ate_2000 = 0
total_geral = 0

while True:
    ano = int(input("Digite o ano do veículo: "))

    if ano <= 2000:
        desconto = 0.12
        total_carros_ate_2000 += 1
    else:
        desconto = 0.07
    
    valor_carro = float(input("Digite o valor do carro: "))
    valor_desconto = valor_carro * desconto
    valor_pago = valor_carro - valor_desconto
    total_geral += valor_pago

    print(f"Desconto: R$ {valor_desconto:.2f}")
    print(f"Valor a ser pago: R$ {valor_pago:.2f}")

    continuar = input("Deseja continuar calculando desconto? (S/N): ")
    if continuar.strip().upper() != "S":
        break

print(f"Total de carros até 2000: {total_carros_ate_2000}")
print(f"Total geral a ser pago: R$ {total_geral:.2f}")
