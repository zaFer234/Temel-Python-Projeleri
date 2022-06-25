import json
import code
from random import randint

class kayıt ():
    def __init__(self):
        self.menu()
        self.kayıt = []
        self.giriş = True
        self.çıkış = False

    def menu (self):
        print("1.KAYIT OLMA \n"
              "2.GİRİŞ \n"
              "3.ŞİFREMİ UNUTTUM\n"
              "4.ÇIKIŞ")
        sayı = int(input("YAPMAK İSTEDİĞİNİZ RAKAMI GİRİNİZ:"))



        if sayı == 1:
            epost = input("EPOSTA GİRİNİZ:")
            şifre = input("ŞİFRE GİRİNİZ:")
            ştekrar = input("ŞİFRE TEKRAR YAZINIZ:")
            dkodu = str(randint(1000,9999))


            with open("kod.txt","w") as dosya:
                dosya.write(dkodu)
            ddkodu = input("GELEN DOĞRULAMA KODUNU GİRİNİZ:")
            if şifre == ştekrar and ddkodu == dkodu:
                print("****KAYIT BAŞARILI****")
                with open("kkayıt.jsaon","a") as kdosya:
                    json.dump("kullanici---",kdosya)
                    json.dump(epost,kdosya)
                    json.dump(şifre,kdosya)
            else:
                print("İŞLEM HATALI!!")



        elif sayı == 2:
            epostg = input("EPOSTA GİRİNİZ:")
            şifreg = input("ŞİFRE GİRİNİZ:")
            dkodu = str(randint(1000, 9999))
            with open("kod.txt", "w") as dosya:
                dosya.write(dkodu)
            ddkodu = input("GELEN DOĞRULAMA KODUNU GİRİNİZ:")
            if dkodu == ddkodu:
                print("BAŞARILI")




        elif sayı == 3:
            input("EPOSTA ADRESİNİ GİRİNİZ:")
            dkodu = str(randint(1000, 9999))
            with open("kod.txt", "w") as dosya:
                dosya.write(dkodu)
            ddkodu = input("GELEN DOĞRULAMA KODUNU GİRİNİZ:")
            if dkodu == ddkodu:
                input("YENİ ŞİFRENİZİ GİRİNİZ:")
                print("İŞLEM BAŞARILI")


        else:
            print("ÇIKIŞ YAPILDI")

kayıt()