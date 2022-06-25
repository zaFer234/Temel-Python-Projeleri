ilk = int(input("İlk sayıyı giriniz:"))
iki = int(input("İkinci sayıyı giriniz:"))
def ekok(x,y):
    ekok = x*y
    for i in range(ekok,max(x,y)-1,-1):
        if i % x == 0 and i % y == 0:
            ekok = i
    return ekok
print(ekok(ilk,iki))


