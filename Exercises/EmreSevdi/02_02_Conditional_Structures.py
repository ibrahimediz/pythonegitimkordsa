aci1 = input("açıyı giriniz:")
aci2 = input("açıyı giriniz:")
aci3 = 180 - (aci1 + aci2)

if aci3 == 90:
    print("Dik açılı üçgen")
if aci1 == aci2 == aci3:
    print("Eşkenar üçgen")
if aci1 == aci2 != aci3:
    print("İkizkenar üçgen")
if aci1 != aci2 != aci3:
    print("çeşitkenar üçgen")
elif (aci1 + aci2 + aci3) > 180:
    print("yanlış girdiniz")
else:
    print("ikizkenar üçgen")