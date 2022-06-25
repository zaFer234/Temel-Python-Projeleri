from random import randint

x = randint(1,101)
dur = 1
oyun = True
hak = 7
while oyun:
    x = randint(1, 101)
    while dur<8:
        dur = dur + 1
        sayı =  int(input("1-100 arası sayı tahmin ediniz({} hakkınız var):".format(hak)))
        hak = hak - 1
        if sayı == x:
            print("Doğru tahmin.")
            break
        elif sayı != x and sayı < x:
            print("Yanlış tahmin.")
            print("Tahmininizi arttırınız.")
        elif sayı > x:
            print("Yanlış tahmin.")
            print("Tahmininizi azaltınız.")
    print(x)
    devam = input("Tekrar oynamak istermisiniz: (e= evet h= hayır)")
    hak = 7
    dur = 1
    if devam == "e":
        oyun = True
    else:
        oyun = False