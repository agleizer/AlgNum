# Função para calcular a norma L2 (distância euclidiana) entre dois vetores
def calcular_norma(vetor1, vetor2):
    soma = 0.0
    for i in range(len(vetor1)):
        soma += (vetor1[i] - vetor2[i]) ** 2
    return soma ** 0.5

# Função principal para resolver um sistema de equações lineares usando o método de Jacobi
def metodo_jacobi(A, b, XO, TOL, N):
    """
    A: Matriz de coeficientes (matriz quadrada)
    b: Vetor de termos independentes
    XO: Aproximação inicial para a solução
    TOL: Tolerância para a condição de parada
    N: Número máximo de iterações permitidas
    """
    
    n = len(b)  # Número de equações/variáveis
    X = XO[:]   # Vetor para armazenar a solução atual (cópia de XO)
    
    # Passo 1: Inicializar o número de iterações
    k = 1
    
    # Passo 2: Loop principal do método de Jacobi
    while k <= N:
        # Criar um novo vetor para armazenar a solução da iteração atual
        X_novo = [0.0] * n
        
        # Passo 3: Atualizar cada valor x_i para a nova iteração
        for i in range(n):
            # Inicializar o somatório para a equação i
            soma = 0.0
            for j in range(n):
                if i != j:
                    soma += A[i][j] * XO[j]
            
            # Calcular o novo valor de x_i
            X_novo[i] = (b[i] - soma) / A[i][i]
        
        # Passo 4: Verificar se a solução está dentro da tolerância
        if calcular_norma(X_novo, XO) < TOL:
            print("O procedimento foi bem-sucedido. Solução encontrada:")
            return X_novo
        
        # Passo 5: Incrementar o número de iterações
        k += 1
        
        # Passo 6: Atualizar XO para ser a solução calculada nesta iteração
        XO = X_novo[:]
    
    # Passo 7: Se o número máximo de iterações for excedido
    print("Número máximo de iterações excedido. O procedimento falhou.")
    return None

# Exemplo de uso:
# Matriz de coeficientes A (3x3), vetor de termos independentes b, e aproximação inicial XO
A = [[4, -1, 0, 0],
     [-1, 4, -1, 0],
     [0, -1, 4, -1],
     [0, 0, -1, 3]]

b = [15, 10, 10, 10]
XO = [0, 0, 0, 0]
TOL = 1e-6  # Tolerância
N = 100     # Número máximo de iterações

# Chamar a função para encontrar a solução
solucao = metodo_jacobi(A, b, XO, TOL, N)

if solucao:
    print(solucao)
