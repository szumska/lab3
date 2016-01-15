#  Wzorowane na przykładzie Rona Zacharskiego
#

from math import sqrt


users = {
        "Ania": 
            {"Blues Traveler": 1.,
            "Broken Bells": 1.5,
            "Norah Jones": 2,
            "Deadmau5": 2.5,
            "Phoenix": 3.0,
            "Slightly Stoopid": .5,
            "The Strokes": 0.0,
            "Vampire Weekend": 2.0},
         "Bonia":
            {"Blues Traveler": 4.0,
            "Broken Bells": 4.5, 
            "Norah Jones": 5.0,
            "Deadmau5": 5.5, 
            "Phoenix": 6.0, 
            "Slightly Stoopid": 3.5, 
            "The Strokes": 2.0,
            "Vampire Weekend": 5.0}
        }

        
def manhattan(rating1, rating2):
    
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają… wspólnych elementów"""
       
    # TODO: wpisz kod
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    odleglosc = 0
    udaloSiePorownac = False

    for klucz in klucze1:
        if klucz in rating2.keys():
            udaloSiePorownac = True
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz])

    if (udaloSiePorownac==True):
        return odleglosc
    else:
        return -1

def pearson(rating1, rating2):
    korelacja=0
    udaloSiePorownac = False
    klucze1 = rating1.keys()
    klucze2 = rating2.keys() 
    n=0
    suma1=0
    suma2=0
    suma3=0
    suma4=0
    suma5=0
    for klucz in klucze1:
        if klucz in rating2.keys():
            udaloSiePorownac = True
            suma1=suma1+rating1[klucz]*rating2[klucz]
            suma2=suma2+rating1[klucz]
            suma3=suma3+rating2[klucz]
            suma4=suma4+pow(rating1[klucz],2)
            suma5=suma5+pow(rating2[klucz],2)
            n+=1
    korelacja=(suma1-(suma2*suma3)/n)/(sqrt(suma4-pow(suma2,2)/n)*sqrt(suma5-pow(suma3,2)/n))
    if (udaloSiePorownac==True):
        return korelacja
    else:
        return -1



print ("Odleglosc manhattan między preferencjami Boni  i Ani to: " + str(manhattan(users["Bonia"],users["Ania"])))
print ("Korelacja między ich preferencjami to: " + str(pearson(users["Bonia"],users["Ania"])))
