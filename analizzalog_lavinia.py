# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 15:20:10 2021

@author: Lavinia
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 10:12:51 2021

@author: Lavinia
"""
"""Scrivere un programma Python che legge una lista di log anonimizzati da un file.

Ciascun elemento della lista di log è costituito dalle seguenti otto informazioni:

Data/Ora
Identificativo unico dell’utente
Contesto dell’evento
Componente
Evento
Descrizione
Origine
Indirizzo IP
L'obiettivo è quello di calcolare per ogni utente un vettore di feature e salvare i dati sia in un foglio excel, sia in formato json

Possibili feature per ogni utente

numero totale di eventi
quante volte si è verificato ciascun evento
data primo evento
data ultimo evento
numero di giorni tra il primo e l'ultimo evento
media e varianza del numero eventi in una settimana (da lunedi' a domenica)
altre features a piacere"""

"""importazione del modulo json"""
import json 

"""sottoprogramma per la gestione degli errori nell'esecuzione del programma:
    il sottoprogramma stampa un messaggio di errore ed esce dal programma"""

def error(message):
    print(message)
    # exit()

"""leggo il file json"""

fin=open('log.json')
lista_log=json.load(fin)

        
"""sottoprogramma che scrive dati in un file json e gestisce le eccezioni, al sottoprogramma
vengono passati come parametri l'oggetto json da scrivere nel file e il nome del file da scrivere 
l'indentazione viene passata per avere una visualizzazione migliore del file"""

def write_json(data,file_name, indent=3):
    try:
        fout=open(file_name,'w')
        json.dump(data,fout)
        fout.close()
    except OSError as message:
        error(message)
        
    """sottoprogramma che calcola per ogni utente il numero totale di occorrenze dalla lista di log"""
    """al sottoprogramma è passato come parametro la lista dei log e resistuisve un dizionario di 
    dizionari con il codice utente e il numero di occorrenze per ogni utente"""
def totale_occorrenze(lista_log):
        tab_occorrenze={}         
        """ho creato la tabella delle occorrenze che è un dizionario inizialmente vuoto,
        se il log non è presente lo aggiunge con occorrenza 1, se è già presente ne aumenta 
        di 1 l'occorrenza""" 
        for log in lista_log:
            if not log[1] in tab_occorrenze:
                tab_occorrenze[(log[1])]={}
                tab_occorrenze[(log[1])]['totaleoccorrenze']=1
            else:
                tab_occorrenze[(log[1])]['totaleoccorrenze']+=1
        return tab_occorrenze
        
"""sottoprogramma che cacola le occorrenze per ogni signolo evento, riceve come parametri 
la lista dei log e la tabella delle occorrenze dei log e resitutisce la lista dei log e il
dizionario con le occorrenze per ogni utente"""
def occorrenze_eventi(lista_log,tab_occorrenze):
    for log in lista_log:
            if not log[4] in tab_occorrenze[log[1]]:
                tab_occorrenze[log[1]][log[4]]=1
            else:
                    tab_occorrenze[log[1]][log[4]]+=1
    return tab_occorrenze
          
"""sottoprogramma che calcola le date in cui un utente ha eseguito una determinata azione,
riceve come paramteri la tabella delle occorrenze"""
"""la tabella delle occorrenze è un dizionario di dizionari che contiene per ogni codice
utente, il numero di occorrenze dell'utente e il numero di occorrenze per ogni evento"""
"""il sottoprogramma restituisce la stessa tabella passata come parametro, riportando 
le date in cui un'utente ha effettutato un evento"""

def date_occorrenze(tab_occorrenze):
  for key in tab_occorrenze:
        tab_occorrenze[key]['date']=[]
        for log in lista_log:
            data = log[0].split()
            if log[1]==key:
                tab_occorrenze[key]['date']+=[data[0]]
            return tab_occorrenze
#It can be useful for the next calculation of first date, last date etc.

def x(tab_occorrenze):
    for key in tab_occorrenze:
        date_eventi = tab_occorrenze[key]['date']
        tab_occorrenze[key]['ultima_data']=date_eventi[0]
        tab_occorrenze[key]['prima_data']=date_eventi[-1]
        return tab_occorrenze
                        

tab_occorrenze =totale_occorrenze(lista_log)
tab_occorrenze=occorrenze_eventi(lista_log,tab_occorrenze)
tab_occorrenze = date_occorrenze(tab_occorrenze)
tab_occorrenze = x(tab_occorrenze)
write_json(tab_occorrenze,'nuovofile.json', indent=3)

print('FINE')
    