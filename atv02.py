def calcular_azulejos(altura_parede, largura_parede, altura_azulejo, largura_azulejo):
    area_parede = altura_parede * largura_parede
    area_azulejo = altura_azulejo * largura_azulejo
    num_azulejos = -(-area_parede / area_azulejo) 
    return num_azulejos


altura_parede = float(input("Digite a altura da parede (em metros): "))
largura_parede = float(input("Digite a largura da parede (em metros): "))
altura_azulejo = float(input("Digite a altura do azulejo (em metros): "))
largura_azulejo = float(input("Digite a largura do azulejo (em metros): "))


numero_azulejos = calcular_azulejos(altura_parede, largura_parede, altura_azulejo, largura_azulejo)


print(f"Serão necessários {numero_azulejos} azulejos para cobrir a parede.")
