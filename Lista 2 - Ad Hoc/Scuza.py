t = int(input())

for a in range(t):
    n, q = map(int, input().split())
    degraus = [int(x) for x in input().split()]
    perguntas = [int(x) for x in input().split()]
    
    acumulados = [0] * n
    maximos = [0] * n

    acumulados[0] = degraus[0]
    maximos[0] = degraus[0]
    
    for i in range(1, n):
        acumulados[i] = acumulados[i - 1] + degraus[i]
        maximos[i] = max(maximos[i - 1], degraus[i])
    
    resultados = []
    for k in perguntas:
        
        esquerda, direita = 0, n - 1
        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            if maximos[meio] <= k:
                esquerda = meio + 1
            else:
                direita = meio - 1
        
        
        if direita >= 0:
            resultados.append(acumulados[direita])
        else:
            resultados.append(0)

    print(" ".join(map(str, resultados)))