# 1. Descreva, em pseudocódigo, um algoritmo para calcular uma aproximação da função:
# f(x) = e^x
# Utilizando a expansão em Série de Taylor truncada mostrada abaixo:
# e^x ≈ Σ (from i=0 to N) (x^i / i!) = 1 + x + (x^2 / 2!) + (x^3 / 3!) + ... + (x^N / N!)

# referencia: e = 2.71828

def exponencial(base, potencia):
    i = 0
    total = 1
    while (i < potencia):
        total = total * base
        i += 1
    return total

def fatorial(num):
    total = 1
    while (num > 0):
        total = total * num
        num = num - 1
    return total

def aproxPotenciaNumEuler(potencia, qtdMaxIteracoes, tolerancia):
    resultado = 0
    i = 0
    while i < qtdMaxIteracoes:
        termo = exponencial(potencia, i) / fatorial(i)
        if (termo < tolerancia):
            return resultado
        resultado += termo
        i += 1
    return resultado

print("Resultado de e^3 com 5 iterações: " + str(aproxPotenciaNumEuler(3, 5, 0.0001)))
print("Resultado de e^3 com 10 iterações: " + str(aproxPotenciaNumEuler(3, 10, 0.0001)))