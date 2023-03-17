def faktoriyonel(sayi):
     if sayi == 0 :
        return : 1
                 return sayi*faktoriyel(sayi-1)




tckimliknosu = "10000000146"
# ktckimliknosu = input("T.C. Kimlik Numaranızı Giriniz:")
if len(tckimliknosu) == 11 and tckimliknosu[0] != "0" and tckimliknosu.isdigit():
    if (sum([int(i) for i in range(0,9,2)])*7 - sum([int(i) for i in range(1,8,2)]))%10 == int(ktckimliknosu[9]):
        
else:
    print("Kural 1,2,3  hatası")  
