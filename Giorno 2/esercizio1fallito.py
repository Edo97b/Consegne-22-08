import math

def calcolaperimetroquadrato(lato):
    return 4 * lato

def calcolaperimetrocerchio(raggio):
    return 2 * math.pi * raggio

def calcolaperimetrorettangolo(base, altezza):
    return 2 * (base + altezza)

def calcola_perimetro():
    print("Scegli una figura geometrica per calcolare il perimetro:")
    print("1. Quadrato")
    print("2. Cerchio")
    print("3. Rettangolo")
    
    scelta = input("Inserisci il numero della tua scelta (1, 2, 3): ")
    
    if scelta == '1':
        lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
        perimetro = lato * 4
        print(f"Il perimetro del quadrato è: {perimetro:.2f} unità.")
        
    elif scelta == '2':
        raggio = float(input("Inserisci il raggio del cerchio: "))
        circonferenza = 2 * math.pi * raggio
        print(f"La circonferenza del cerchio è: {circonferenza:.2f} unità.")
        
    elif scelta == '3':
        base = float(input("Inserisci la base del rettangolo: "))
        altezza = float(input("Inserisci l'altezza del rettangolo: "))
        perimetro = 2 * (base + altezza)
        print(f"Il perimetro del rettangolo è: {perimetro:.2f} unità.")
        
    else:
        print("Scelta non valida. Per favore, inserisci 1, 2 o 3.")