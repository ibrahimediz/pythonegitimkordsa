yas = input("Yaşınızı Giriniz:") # str # input fonk her zaman str cevap döner
if yas.isdigit():
    yas = int(yas) # str veri tipinden int veri tipine dönüştürdü
    if yas > 18:
        print("Kabul Edildi")
    else:
        print("Kabul Edilmedi")