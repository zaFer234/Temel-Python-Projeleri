sayi = int(input("Faktöriyelini Hesaplamak için sayı giriniz:"))
faktöriyel = 1
for i in range(1,sayi+1):
   faktöriyel = faktöriyel * i
print("{}! = ".format(sayi) + str(faktöriyel))