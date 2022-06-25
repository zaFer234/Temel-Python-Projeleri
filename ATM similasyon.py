print("KART VERİNİZ")
para = 2000
print("1.Para yatırınız  -  "
      "2.Para çekiniz  -  "
      "3.Hesap bilgileri  -  "
      "4.Kart iade")
veri = int(input("Yapmak istediğiniz işlem rakamını giriniz:"))
if veri == 1:
    y_miktar = int(input("Tutar giriniz:"))
    print("İşlem yapılıyor")
    para += y_miktar
    print(para)
    print("TL")
    print("KART GERİ VERİLİYOR!")
elif veri == 2:
    x_miktar = int(input("Tutar giriniz:"))
    if x_miktar <= para:
        print("İşlem yapılıyor")
        print("Kalan = ")
        para -= x_miktar
        print(para)
        print("TL")
    elif x_miktar >= para:
        print("Hatalı tutar!  -  "
              "KART GERİ VERİLİYOR")
elif veri == 3:
    print("Ad: Ömer ZAFER  -  "
          "IBAN: Tr23453467095  -  "
          "Şube: Sancaktepe a.ş.")
elif veri == 4:
    print("KART GERİ VERİLİYOR")