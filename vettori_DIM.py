#dati 2 vettori di dimensione DIM riempirli con numeri casuali compresi tra 1 e 10
#e poi dire se i due vettori sono uguali 

import random

def riempi_vettori(a, b, DIM):
    x = 0
    for x in range(DIM):
        a.append(random.randint(1, 10))
        b.append(random.randint(1, 10))
    print(a)
    print(b)
    return a, b

def confronta(a,b, DIM):
    x = 0
    equals = 0
    for x in range(DIM):
        if a[x] == b[x]:
            equals = equals + 1
    if equals == DIM:
        print('I due vettori contengono valori uguali')
    else:
        print('Vettori non uguali')


DIM = int(input(' Dimensione dei vettori'))

a = []
b = []

a, b = riempi_vettori(a, b, DIM)
confronta(a, b, DIM)