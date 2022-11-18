# kullanıcıdan girdi almak
#! karar blokları
#! döngüler
print("2. gün başlangıç")

userInput = input()
print(f"Girilen değer: {userInput}")

#! type conversion
numberStr = "10"
print(type(numberStr))
number = int(numberStr)
print(number)
print(type(number))

userInput = input() #kullanıcıdan input alma
#lessonNote = int(userInput) #tam sayı girebilirsin
lessonNote = float(userInput) #ondalıklı sayı girilebilir
print(f"Ders notunuz: {lessonNote}")

#indent (kendi kendine tab yapar ve satır bir üstteki satıra bağlıdır)
#! karar blokları ile işlem yapma
if lessonNote>50:
    print("Geçtiniz")
elif lessonNote == 50:
    print("Sınırda Geçtiniz")
elif lessonNote == 49:
    print("Sınırda kaldınız")
else:
    print("Kaldınız")
#print("Burası if e bağlı değil her türlü çalışacak")
#! kullanıcıdan vize ve final notları alacak.
#! vize %40 final %60 etkili olacak.
#! vize ve final notları 50.5 gibi ondalıklı sayılar olabilir
#! 0-49 FF
#!50-60 DD
#!60-70CC
#!70-80 BBs
#! 80-100 AA

for i in range(6) #içerisine verilen sayı kadar 0'dan başlayan içerisye verilen sayı kadar integer verir.
print(i)
