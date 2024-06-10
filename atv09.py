# Critérios de reajuste
criterios_reajuste = [
    {"limite_inferior": 0, "limite_superior": 3, "porcentagem": 0.5},
    {"limite_inferior": 3, "limite_superior": 10, "porcentagem": 0.2},
    {"limite_inferior": 10, "limite_superior": 20, "porcentagem": 0.15},
    {"limite_inferior": 20, "limite_superior": float('inf'), "porcentagem": 0.1}
]

# Função para calcular o reajuste salarial
def calcular_reajuste(salario):
    for criterio in criterios_reajuste:
        if salario < criterio["limite_superior"]:
            return salario * (1 + criterio["porcentagem"])

# Número de funcionários
numero_funcionarios = 584

# Leitura e aplicação do reajuste para cada funcionário
for i in range(numero_funcionarios):
    salario_atual = float(input(f"Digite o salário do funcionário {i + 1}: "))
    novo_salario = calcular_reajuste(salario_atual)
    print(f"Novo salário do funcionário {i + 1}: R$ {novo_salario:.2f}")
