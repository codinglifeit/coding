def massimo_intero(N):
    k = 0
    somma = 0
    while(somma <= N):
        somma = somma + (k + 1)
        k = k + 1
    return k -1

print(massimo_intero(30))