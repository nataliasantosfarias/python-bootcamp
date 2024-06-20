opcao = float(input("Informe o código para o atendimento:\n OPÇÃO [1] - SACAR \n OPÇÃO [2] Estrato: "))
resultado = opcao
print("Muito bem, você digitou a opção : ",resultado)



if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    
elif opcao == 2:
    print("Exibindo o extrato...") # Se não Se, necessário quando houver mais de um condição
    
else:
    sys.exit("Opção inválida!")









# Condicional para exibir interação do usário com o sistema