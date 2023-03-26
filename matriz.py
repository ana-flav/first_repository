y= int(input("qtd linhas:")) 
 = [0]*y #cria as linhas
x = int(input("qtd colunas: ")) 
matriz = [linha_com_zeros] * x 
print(matriz) 
for coluna in range(x):
    linha = [] #declaro que é uma lista
    for line in range(y):
        numero = int(
            input("informe os valores para preencher na coluna {} e linha {} :".format(coluna, line)))
        linha.append(numero) 
    matriz[coluna] = linha 
print(matriz)