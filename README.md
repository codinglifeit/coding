# coding
a folder full of programming exercises useful for consolidating one's knowledge

You can find all the exercises on the Codinglife.it blog. All the exercises are in Python but you can use the programming language of your choice.
If you want to create a powerful algorithm, you can create a very accurate analysis and detailed example to solve all the points that the problem presents to you.

For example:

Problema : 

Date due liste di numeri di dimensioni DIM, riempirle con casuali compresi da 1 a 10 e successivamente verificare se contengono numeri uguali.

Analisi  : 

L’algoritmo che dobbiamo creare deve, innanzitutto, riempire due liste di numeri con numeri casuali compresi tra 1 e 10. Per fare ciò esistono, per qualsiasi tipo di    linguaggio di programmazione, delle apposite librerie e funzioni. Una volta costruite le liste andranno confrontate per verificare se corrispondono e quindi i numeri al loro interno sono uguali. In caso affermativo mostreremo un messaggio che indica l’effettiva corrispondenza degl’indici delle liste.

Risoluzione : 

Per risolvere l’algortimo abbiamo bisogno di creare due funzioni, la prima che permette l’inserimento dei random all’interno delle liste di numeri e la seconda che procede con il confronto. Per riempire le liste, prima di tutto, dobbiamo conoscere il numero che definisce la grandezza delle due, ovvero DIM. Dopo averlo letto da tastiera, passiamo come argomento della funzione “riempi_liste ( )“, le due liste e DIM.

Utilizzando Python, come nel mio caso, dovremmo importare la libreria random attraverso il metodo import, e successivemante utilizzeremo tale libreria al momento del riempimento delle liste tramite funzione append che va a inserire il numero casuale all’interno della lista.  

Attraverso la funzione “confronta_liste ( )” , tramite l’utlizzo di un ciclo for con range DIM, metteremo a confronto le due liste di numeri.
