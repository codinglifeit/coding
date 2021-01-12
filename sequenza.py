#scrivere un programma che legge una sequenza di numeri terminata da 0 (zero) ed alla fine dice se i numeri
#erano in ordine crescente, decrescente o misto (lo zero NON c’entra) 
def sequenza():
    lista_numeri = []
    n = int(input())
    while (n != 0):
        lista_numeri.append(n)
        n = int(input())


    return lista_numeri

def ordine(lista_numeri):
    crescente = 0
    decrescente = 0
    misto = 0
    for i in range (0, len(lista_numeri) - 1):
        cont_lista = i
        if lista_numeri[i] < lista_numeri[i+1]:
            crescente = crescente + 1
        elif lista_numeri[i] > lista_numeri[i+1]:
            decrescente = decrescente + 1
        else: 
            misto = misto + 1
    
    if crescente == i + 1 : 
        print(' Lista crescente ')
    elif decrescente == i + 1:
        print('Lista decrescente')
    else:
        print('Lista mista')

lista_numeri = sequenza()
ordine(lista_numeri)