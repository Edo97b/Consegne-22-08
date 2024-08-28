def perimetro():
    print("Calcolo del perimetro di una figura")
    print("""
    - 1: Quadrato
    - 2: Rettangolo
    - 3: Cerchio
    """)

    print('Inserire la scelta:')
    scelta = int(input("- "))
    if scelta == 1:
        print("Hai selezionato il Quadrato")
        lato = float(input("Inserisci il valore del lato - "))
        print("Il perimetro del Quadrato", "è:", lato * 4)
    elif scelta == 2:
        print("Hai selezionato il del Rettangolo")
        base = float(input('Inserisci il valore della base - '))
        altezza = float(input('Inserisci il valore dell\'altezza - '))
        print("Il perimetro del Rettangolo è:", base * 2 + altezza * 2)
    elif scelta == 3:
        print("Hai selezionato il Cerchio")
        r = float(input('Inserisci il valore del raggio - '))
        print("Il perimetro del Cerchio è:", 2 * r * 3.14)
    else:
        print("Inserire una scelta valida")

perimetro()