isim = input("Adınız nedir? ")

şehirler = ["İstanbul", "Ankara", "İzmir", "Bursa", "Adana", "Antalya", "Konya", "Kayseri", "Trabzon", "Gaziantep"]
şehir = random.choice(şehirler)

if şehir == "İstanbul":
    print(isim + ", tahminime göre şu anda İstanbul'dasınız.")
elif şehir == "Ankara":
    print(isim + ", tahminime göre şu anda Ankara'dasınız.")
elif şehir == "İzmir":
    print(isim + ", tahminime göre şu anda İzmir'desiniz.")
else:
    print(isim + ", tahminime göre şu anda " + şehir + " şehrinde olabilirsiniz.")




