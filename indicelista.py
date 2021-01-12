#Scrivi una funzione a cui vengono passati come parametro un elemento e una lista di elementi, e che ti dica in output se l'elemento passato sia presente o meno nella lista.
#Qualora l'elemento sia presente nella lista, la funzione dovrà inoltre comunicarci l'indice dell'elemento.



def controllo_elemento(elemento, lista):
    lista_elementi_trovati = []
    elementi_trovati = 0
    for i in range (0, len(lista)):
        if int(lista[i]) == int(elemento):
            elementi_trovati = elementi_trovati + 1
            lista_elementi_trovati.append(i)

    if elementi_trovati >= 1 :
        print('TRUE', elementi_trovati, 'volte')
        print('Posizioni:', lista_elementi_trovati)
    else:
        print('FALSE')

def leggi_lista():
    lista = []
    n = int(input())
    while (n != 0):
        lista.append(n)
        n = int(input())

    return lista

print('leggi lista numeri - termina con 0')
lista = leggi_lista()

elemento = input('leggi numero da trovare')
controllo_elemento(elemento, lista)
