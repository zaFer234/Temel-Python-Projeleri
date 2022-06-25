#### eposta sistemi####
'''
kadı = input("Kullannıcı adını giriniz:")
şifre = input("Şifreyi giriniz:")
dkkullanıcı = "zafer"
dşifre = "12345"
if kadı == dkkullanıcı and şifre == dşifre:
    print("BAŞARILI")
elif kadı == dkkullanıcı:
    print("ŞİFRE HATALI!.")
elif şifre == dşifre:
    print("KULLANICI ADI HATALI!")
else:
    print("HATALI GİRİŞ YAPTINIZ!")


#####sayı 2 ye bölünme#####
##
listem = []
for i in range(10):
    listem.append(i)
    #print(i)
    if i%2 == 0:
        print(i)


######2 kat alma#######
sayılar = [1,2,3,4,5]
yeni_s = []
for i in sayılar:
    yeni_s.append(i * 2)
print(yeni_s)



toplam = 0
listem = [0,1,2,3,4,5,6,7,8,9]
for i in range(10):
    if listem[i]%2 == 0:
        toplam = toplam + listem[i]
print(toplam)




def toplama(u,ı,p,l,ş):
    toplm = u+ı+l+ş+p
    print(toplm)
toplama(1,2,3,4,5)


def çıkarma(a,s,d,f,g):
    çıkarm = a-s-d-f-g
    print(çıkarm)
çıkarma(1,2,3,4,5)


def çarpma(v,b,n,m,k):
    çarp =v*b*n*m*k
    print(çarp)
çarpma(1,2,3,4,5)


def bölme(w,e,r,t,y):
    böl = w/e/r/t/y
    print(böl)
bölme(1,2,3,4,5)

from _datetime import datetime
print(datetime.utcnow())
'''
