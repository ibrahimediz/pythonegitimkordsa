import random

ad = input("Adınız nedir? ")

şehirler = ["İstanbul", "Ankara", "İzmir", "Bursa", "Adana", "Antalya", "Konya", "Kayseri", "Trabzon", "Gaziantep"]
şehir = random.choice(şehirler)

if şehir == "İstanbul":
    print(ad + ", tahminime göre şu anda İstanbul'dasınız.")
elif şehir == "Ankara":
    print(ad + ", tahminime göre şu anda Ankara'dasınız.")
elif şehir == "İzmir":
    print(ad + ", tahminime göre şu anda İzmir'desiniz.")
else:
    print(ad + ", tahminime göre şu anda " + şehir + " şehrinde olabilirsiniz.")

#######################################################################
aci1 = (input("Birinci açiyi girin: "))
aci2 = (input("İkinci  açiyi girin: "))

if aci1 + aci2 >= 180:
    print("Hata: Açıların toplamı 180'den küçük veya eşit olmalıdır!")
else:
    if aci1 == aci2:
        print("İkizkenar üçgen")
    elif aci1 == 90 or aci2 == 90 or (180 - aci1 - aci2) == 90:
        print("Dik üçgen")
    elif  aci1 == aci2 == 60:
        print("Eşkenar üçgen")
    else:
        print("Çeşitkenar üçgen")
