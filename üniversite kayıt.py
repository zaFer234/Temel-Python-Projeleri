import sqlite3

baglanti = sqlite3.connect("ögrenciler.db")
ımlec = baglanti.cursor()
ımlec.execute("CREATE TABLE IF NOT EXISTS bilgiler(İSİM TEXT,SOYAD TEXT,SINIF TEXT,BÖLÜM TXT,NUMARA İNT,DURUM TEXT,ID İNT) ")


class üniversite():
    def __init__(self):
        self.menu()



    def menu (self):
        print("TAİHL KAYIT SİSTEMİ")

        print('''
1-ÖĞRENCİ KAYIT
2-ÖĞRENCİ GÖSTER
3-ÖĞRENCİ SİL
4-ÖĞRENCİ DÜZENLE
      
        ''')
        while True:
            try:
                self.menu = int(input("YAPMAK İSTEDİĞİNİZ İŞLEM RAKAMINI GİRİNİZ:"))
                if 0 < self.menu < 5:
                    break
            except:
                print("LÜTFEN DOĞRU GİRİNİZ!:")

        if self.menu == 1:
            ad = input("ÖĞRENCİ İSMİNİ GİRİNİZ:")
            soyisim = input("ÖĞRENCİ SOYİSMİNİ GİRİNİZ:")
            sinif = input("ÖĞRENCİNİN SINIFINI GİRİNİZ:")
            bolum = input("ÖĞRENCİNİN BÖLÜMÜNÜ GİRİNİZ:")
            no = int(input("ÖĞRENCİNİN NUMARASINI GİRİNİZ:"))
            drum = input("ÖĞRENCİNİN DURUMUNU GİRİNİZ:")
            id = int(input("ÖĞRENCİNİN ID GİRİNİZ:"))

            ımlec.execute("INSERT INTO bilgiler VALUES('{}','{}','{}','{}',{} ,'{}',{})".format(ad,soyisim,sinif,bolum,no,drum,id))
            baglanti.commit()
            baglanti.close()
            print("***KAYIT BAŞARILI***")


        elif self.menu == 2:

          sınıf =  input("HANGİ SINIFI GÖRMEK İSTERSİNİZ:")

          ımlec.execute("SELECT * from bilgiler WHERE sınıf == '{}' ".format(sınıf))

          for veri in ımlec.fetchall():
              print(veri)

          baglanti.commit()
          baglanti.close()


        elif self.menu == 3:

            sil = int(input("SİLMEK İSSTEDİĞİNİZ ÖĞRENCİNİN ID GİRİNİZ:"))

            ımlec.execute("DELETE FROM bilgiler WHERE ıd == '{}' ".format(sil))

            print("***SİLME İŞLEMİ BAŞARILI***")

            baglanti.commit()
            baglanti.close()



        else:
            disim = input("GÜNCELLEMEK İSTEDİĞİNİZ KİŞİNİN İSMİNİ GİRİNİZ:")
            güncel = input("HANGİ BİLGİYİ DEĞİŞTİRMEK İSTİYORSUNUZ(sınıf,bölüm,numara,durum,ıd):")
            ygüncel = input("YENİ BİLGİYİ GİRİNİZ:")

            ımlec.execute("UPDATE bilgiler SET '{}' = '{}' WHERE isim = '{}'".format(güncel,ygüncel,disim))

            baglanti.commit()
            baglanti.close()

            print("***{} GÜNCELLENDİ***".format(güncel).upper())


üniversite()