lista = [1, 30, 21, 2, 9, 65, 34]
pares = [ ]
    

for lista_auxiliar in lista:
    if lista_auxiliar % 2 == 0:
        pares.append(lista_auxiliar)
        print("Agora temos uma lista de números pares\n", pares)



# Este código Python está a iterar sobre cada elemento da lista `lista`. Para cada elemento, ele verifica se
# o elemento é divisível por 2 (i.e., se é um número par) usando a condição `lista_auxiliar
# % 2 == 0`. Se a condição for verdadeira, o elemento é adicionado à lista `pares` utilizando o método `append()`
# método. Finalmente, ele imprime o estado atual da lista `pares` após cada número par ser adicionado a
# adicionado a ela.