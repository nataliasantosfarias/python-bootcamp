def exibir_mensagem():
    print("Olá mundo!")

#Essa função possui um argumento
def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}!")
    
def exibir_mensagem3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")
    

exibir_mensagem()    
exibir_mensagem2("NAti") # Passado o argummento da função