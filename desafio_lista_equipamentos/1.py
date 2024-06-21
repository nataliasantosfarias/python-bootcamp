def gerenciar_equipamentos():
    itens = []

    for i in range(3):
        item = input(f" Insira um ítem na lista {i+1} : ")
        itens.append(item)  # Adiciona o item à lista "itens"

# Exibe a lista de itens
    print("Lista de Equipamentos:")  
    for item in itens:
        # Loop que percorre cada item na lista "itens"
        print(f"- {item}")
        
gerenciar_equipamentos()

#O objetivo é criar um solução que permita aos usuários inserir informações sobre os equipamentos que serão cadastrados na rede, em seguida, exibir essa lista de equipamentos. Crie uma Lista para armazenar esses equipamentos e depois um loop para solicitar ao usuário inserir até três equipamentos.

# Entrada
# O programa solicitará ao usuário que insira uma lista com três equipamentos para adicionar a rede.

# Saída
# Após a entrada dos itens, o programa exibirá a lista de equipamentos inseridos pelo usuário. Cada equipamento será listado com um prefixo ( - ) de marcação para melhor organização.