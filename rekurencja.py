# def silnia(liczba):
#     if liczba==0:
#         return 1
#     else:
#         return liczba * silnia(liczba-1) #wywołanie tej funkcji w funkcji
# wynik=silnia(3)
# print(wynik)

def sumowanie (listaLiczb):
    if len(listaLiczb) > 0:
        print(listaLiczb)
        return listaLiczb[0]+sumowanie(listaLiczb[1:]) #musi byc o 0
    else:
        return 0

lista=[1 ,2 ,3 ,4 ,5]
wynik=sumowanie(lista)
print(wynik)

