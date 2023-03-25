y= int(input("tamanho total da  sua matriz :")) #se sua matriz for de 3 linhas e 3 colunas digite 3
linha = [0]*y # aqui vc criar a qtd de linhas para sua matriz e uma lista
matriz = [linha] * y #tecnicamente eu crio minhas colunas aqui dentro, estou repetindo minha lista linha em 3 vezes
print(matriz) 
for line in range(y):
    linha = [] #declaro que é uma lista
    for coluna in range(y):
        numero = int(
            input("informe os valores para preencher na linha {} e coluna {} :".format(line, coluna)))
        linha.append(numero) #adiciona o valor no final da lista  linha
    matriz[line] = linha # na posição na minha matriz eu vou colocando os valores da minha lista linha
print(matriz)