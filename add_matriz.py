m = int(input("qtd colunas:")) 
colunas= [0]*m 
n = int(input("qtd linhas: ")) 
matriz = [colunas] * n 
print(matriz) 

for l in range(n):
    list = [] #declaro que é uma lista
    for c in range(m):
        numero = int(
            input("informe os valores para preencher na coluna {} e linha {} :".format(c, l)))
        list.append(numero) 
    matriz[l] = list 

print(matriz)
print(matriz[1][0])