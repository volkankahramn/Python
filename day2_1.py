#for i in range(6):
 #   print(i)

#students = ["Nilüfer","Özlem","Berk","Zakir"]
#for i in students:
 #   print(i)
    #! infinite loop
    #while true
    # print("I am infinitel")

#i = 0
#while i < 10:
   # print(i)
    #i+=1
lessonCount = int(input("Kaç ders için hesaplama yapmak istiyorsunuz?:"))

girilenVize = []
girilenFinal = []
girilenOrtalama = []
gecilenDersSayisi = 0

for i in range(lessonCount):
    vizeNotu = int(input(f"{i+1}. dersin Vize notunu giriniz:"))
    finalNotu = int(input(f"{i+1}. dersin Final notunu giriniz:"))
    ortalamaNotu = (vizeNotu * 0.4) + (finalNotu * 0.6)
    girilenVize.append(vizeNotu)
    girilenFinal.append(finalNotu)
    girilenOrtalama.append(ortalamaNotu)
if(ortalamaNotu) >=50:
    gecilenDersSayisi +=1
print(f"Vize notlarınız: {girilenVize}")
print(f"Final notlarınız: {girilenFinal}")
print(f"Ortalama notlarınız: {girilenOrtalama}")
print(f"{lessonCount} adet dersin {gecilenDersSayisi} kadarından başarılı olunmuştur.")

