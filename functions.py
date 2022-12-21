#fonksiyonlar
sayi1 = 1
sayi2 = 2
#toplam = topla(sayi1, sayi2)

#toplam2 = topla(5, 10)

#def => definition 
#parametre => fonskiyon çağırılırken verilmesi istenilen değerler.
def topla(sayi1, sayi2):
    toplam = sayi1 + sayi2
    print(toplam)

topla(1,2)

def passsedOrNot(note)
    if note < 50:
        return False
    else:
        return True
if passsedOrNot(60):
    print("Geçtiniz")
else:
    print("Kaldınız")