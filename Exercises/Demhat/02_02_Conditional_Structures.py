"""name = ["Ali","Berk","Demhat","Emre","Hatice"]

userName = input("Lütfen isminizi giriniz:")

if userName in name:
    if userName == "Ali":
        print("Adana")
    if userName == "Berk":
        print("Bursa")
    if userName == "Demhat":
        print("Diyarbakır")
    if userName == "Emre":
        print("Edirne")
    if userName == "Hatice":
        print("Hatay")
else:
    print("Kullanıcı bulunamadı!")
    """

firstAngel = float(input("Please enter first anngle:"))
secondAngel = float(input("Please enter second angle:"))
thirdAngle = 180 - (firstAngel+secondAngel)
result = firstAngel+secondAngel+thirdAngle
if result == 180:
    if firstAngel == secondAngel or firstAngel == thirdAngle or secondAngel == thirdAngle:
        print("Bu bir ikizkenar üçgendir:")
    if firstAngel != secondAngel and firstAngel != thirdAngle and secondAngel != thirdAngle:
        print("Bu bir çeşitkenar üçgendir:")
    if firstAngel == 90 or secondAngel == 90 or thirdAngle == 90:
        print("Bu bir dik üçgendir:")

else:
    print("Bir üçgenin iç açıları toplamı 180 olmak zorundadır!")