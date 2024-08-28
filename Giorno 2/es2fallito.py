import math

def calcolaperimetroquadrato(lato):
    return 4 * lato

def calcolaperimetrocerchio(raggio):
    return 2 * math.pi * raggio

def calcolaperimetrorettangolo(base, altezza):
    return 2 * (base + altezza)

def main():
    print("Scegli la figura geometrica per calcolare il perimetro:")
    print("1. Quadrato")
    print("2. Cerchio")
    print("3. Rettangolo")
    
    scelta = input("Inserisci il numero corrispondente alla figura (1/2/3): ")

    if scelta == '1':
        lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
        perimetro = calcolaperimetroquadrato(lato)
        print(f"Il perimetro del quadrato è: {perimetro}")

    elif scelta == '2':
        raggio = float(input("Inserisci il raggio del cerchio: "))
        perimetro = calcolaperimetrocerchio(raggio)
        print(f"La circonferenza del cerchio è: {perimetro}")

    elif scelta == '3':
        base = float(input("Inserisci la base del rettangolo: "))
        altezza = float(input("Inserisci l'altezza del rettangolo: "))
        perimetro = calcolaperimetrorettangolo(base, altezza)
        print(f"Il perimetro del rettangolo è: {perimetro}")

    else:
        print("Scelta non valida. Riprova.")

if __name__== "__main":
    main()