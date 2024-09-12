def calcularErro(vetor1, vetor2):
    maxDiferenca = 0.0
    for i in range(len(vetor1)):
        diferenca = abs(vetor1[i] - vetor2[i])
        if diferenca > maxDiferenca:
            maxDiferenca = diferenca
    return maxDiferenca

# func para resolver um sistema linear usando Jacobi
def metodoJacobi(coefsSistema, termosIndSistema, tamanho, vetorSolucao, tolerancia, iteracoesMax):
    k = 1
    # loop que rodará até a qtd máxima de iterações, a não ser que cheguemos a um resultado antes
    while k <= iteracoesMax:
        # novo vetor para armazenar temporáriamente a aproximação da iteração atual
        novaSolucao = [0.0] * tamanho
        
        # loop somatória (processo iterativo de aproximação)
        for i in range(tamanho):
            soma = 0.0
            for j in range(tamanho):
                if i != j:
                    # Xn * CHUTEn
                    soma += coefsSistema[i][j] * vetorSolucao[j]
            
            # novo valor de x_i = isolar o termo Xi do lado esquerdo = subtrair o Xn * chute e dividir pelo coef.
            if (coefsSistema[i][i]) == 0:
                print("Erro! Existe coeficiente = 0 na diagonal principal.")
                return None
            novaSolucao[i] = (termosIndSistema[i] - soma) / coefsSistema[i][i]
        
        # verificar se a solução está dentro da tolerância
        if calcularErro(novaSolucao, vetorSolucao) < tolerancia:
            print("Solução encontrada:")
            return novaSolucao
        
        k += 1
        
        # atualizar vetorSolucao com a aproximação mais recente
        vetorSolucao = novaSolucao[:]
    
    # se chegarmos aqui, não atingimos a tolerância dentro do nuymero de iterações permitido
    print("Erro: o número máximo de iterações excedido.")
    return None

# MAIN

## TESTE COM EXEMPLO DE AULA
# coefsSistema = matriz de coeficientes do sistema
coefsSistema = [[10, -1, 2, 0],
                [-1, 11, -1, 3],
                [2, -1, 10, -1],
                [0, 3, -1, 8]]

# termos independentes
termosIndSistema = [6, 25, -11, 15]

# tamanho do distema
tamanho = len(termosIndSistema)

# XO = chute inicial
vetorSolucao = [0, 0, 0, 0]

# tolerancia
tolerancia = pow(10, -3)

# numero max de iterações
iteracoesMax = 20

# Chamar a função para encontrar a solução
solucao = metodoJacobi(coefsSistema, termosIndSistema, tamanho, vetorSolucao, tolerancia, iteracoesMax)

if solucao:
    print(solucao)

### EXERCICIOS LISTA 3
## EX A

# suspeito que esse não vai funcionar por tem elemento = 0 na diagonal principal
print("\nLista 3, ex. a:")
lista3exA_matrizCoef = [[1, -1, 3],
                        [3, -3, 1],
                        [1, 1, 0]]

lista3exA_termosInd = [2,-1,3]

j = 0
tolerancia = 0.1
while j < 4:
    print("Solução com tolerância = ", tolerancia, ": ")
    vetorSolucao = [0, 0, 0]
    solucao = metodoJacobi(lista3exA_matrizCoef, lista3exA_termosInd, len(lista3exA_termosInd), vetorSolucao, tolerancia, 30)
    print(solucao)
    tolerancia /= 10
    j += 1

## EX B

print("\nLista 3, ex. b:")
lista3exB_matrizCoef = [[2, -1.5, 3],
                        [-1, 0, 2],
                        [4, -4.5, 5]]

lista3exB_termosInd = [1,3,1]

j = 0
tolerancia = 0.1
while j < 4:
    print("Solução com tolerância = ", tolerancia, ": ")
    vetorSolucao = [0, 0, 0]
    solucao = metodoJacobi(lista3exB_matrizCoef, lista3exB_termosInd, len(lista3exB_termosInd), vetorSolucao, tolerancia, 30)
    print(solucao)
    tolerancia /= 10
    j += 1

## EX C

print("\nLista 3, ex. c:")
lista3exC_matrizCoef = [[2, 0, 0, 0],
                        [1, 1.5, 0, 0],
                        [0, -3, 0.5, 0],
                        [2, -2, 1, 1]]

lista3exC_termosInd = [3, 4.5, -6.6, 0.8]

j = 0
tolerancia = 0.1
while j < 4:
    print("Solução com tolerância = ", tolerancia, ": ")
    vetorSolucao = [0, 0, 0, 0]
    solucao = metodoJacobi(lista3exC_matrizCoef, lista3exC_termosInd, len(lista3exC_termosInd), vetorSolucao, tolerancia, 30)
    print(solucao)
    tolerancia /= 10
    j += 1

## EX D

print("\nLista 3, ex. d:")
lista3exD_matrizCoef = [[1, 1, 0, 1],
                        [2, 1, -1, 1],
                        [4, -1, -2, 2],
                        [3, -1, -1, 2]]

lista3exD_termosInd = [2,1,0,3]

j = 0
tolerancia = 0.1
while j < 4:
    print("Solução com tolerância = ", tolerancia, ": ")
    vetorSolucao = [0, 0, 0, 0]
    solucao = metodoJacobi(lista3exD_matrizCoef, lista3exD_termosInd, len(lista3exD_termosInd), vetorSolucao, tolerancia, 30)
    print(solucao)
    tolerancia /= 10
    j += 1

### EXERCICIOS LISTA 4

## EX A

print("\nLista 4, ex. a:")
lista4exA_matrizCoef = [[3, -1, 1],
                        [3, 6, 2],
                        [3, 3, 7]]

lista4exA_termosInd = [1,0,4]

tolerancia = 0.01
print("\nSolução com tolerância = ", tolerancia, ": ")
vetorSolucao = [0, 0, 0]
solucao = metodoJacobi(lista4exA_matrizCoef, lista4exA_termosInd, len(lista4exA_termosInd), vetorSolucao, tolerancia, 30)
print(solucao)

## EX B

print("\nLista 4, ex. b:")
lista4exB_matrizCoef = [[10, -1, 0],
                        [-1, 10, -2],
                        [0, -2, 10]]

lista4exB_termosInd = [9,7,6]

tolerancia = 0.01
print("\nSolução com tolerância = ", tolerancia, ": ")
vetorSolucao = [0, 0, 0]
solucao = metodoJacobi(lista4exB_matrizCoef, lista4exB_termosInd, len(lista4exB_termosInd), vetorSolucao, tolerancia, 30)
print(solucao)

## EX C

print("\nLista 4, ex. c:")
lista4exC_matrizCoef = [[10, 5, 0, 0],
                        [5, 10, -4, 0],
                        [0, -4, 8, -1],
                        [0, 0, -1, 5]]

lista4exC_termosInd = [6, 25, -11, -11]

tolerancia = 0.01
print("\nSolução com tolerância = ", tolerancia, ": ")
vetorSolucao = [0, 0, 0, 0]
solucao = metodoJacobi(lista4exC_matrizCoef, lista4exC_termosInd, len(lista4exC_termosInd), vetorSolucao, tolerancia, 30)
print(solucao)


## EX D

print("\nLista 4, ex. d:")
lista4exD_matrizCoef = [[4, 1, 1, 0, 1],
                        [-1, -3, 1, 1, 0],
                        [2, 1, 5, -1, -1],
                        [-1, -1, -1, 4, 0],
                        [0, 2, -1, 1, 4]]

lista4exD_termosInd = [6, 6, 6, 6, 6]

tolerancia = 0.01
print("\nSolução com tolerância = ", tolerancia, ": ")
vetorSolucao = [0, 0, 0, 0, 0]
solucao = metodoJacobi(lista4exD_matrizCoef, lista4exD_termosInd, len(lista4exD_termosInd), vetorSolucao, tolerancia, 30)
print(solucao)