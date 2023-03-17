kimlikno = input("Tc Kimlik Numaranızı Giriniz:")
def tckimlikkontrolFonk(kimlikno):
    if len(kimlikno) == 11  and kimlikno[0] !="0" and kimlikno.isdigit():
        if sum([int(kimlikno[i]) for i in range(0,9,2)])*7 - sum([int(kimlikno[i]) for i in range(1,8,2)]%10 == kimlikno[9]):
            if sum([int(kimlikno[i]) for i in range(0,10)]) %10 == int(kimlikno[10]):
                return True
tckimlikkontrolFonk(kimlikno)