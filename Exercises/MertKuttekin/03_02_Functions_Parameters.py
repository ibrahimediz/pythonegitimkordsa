kimlikno = input()
def tckimlikkontrolFonk(kimlikno):
    if len(kimlikno) == 11 and kimlikno = int(kimlikno) and kimlikno[0] !="0" and kimlikno.isdigit():
        if sum([for i in range(0,9,2)]*7 - sum([for i in range(1,8,2)]%10 == kimlikno[9])):
            if sum([for i in range(0,10)]) %10 == kimlikno[10]:
                return True
            return False
        return False
    return False
tckimlikkontrolFonk(kimlikno)