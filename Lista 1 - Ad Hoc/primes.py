n = int(input())

numero_primo = n - 2

qtdDivisores = 0
for i in range(1, numero_primo+1):
    if numero_primo%i == 0:
        qtdDivisores += 1

if(qtdDivisores == 2):
    print("2 "+str(numero_primo))
else:
    print("-1")
