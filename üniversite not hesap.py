isim = input("İsim Giriniz:")
vize = int(input("Vize notunu giriniz:"))
final = int(input("Final notunu giriniz:"))
snot = ((vize * 40) / 100) + ((final * 60) / 100)
if 85<= snot <=100:
    print("NOTUNUZ: AA {} {}".format(snot , isim))
if 70<= snot <=84:
    print("NOTUNUZ: BA {} {}".format(snot, isim))
if 60<= snot <=69:
    print("NOTUNUZ: BB {} {}".format(snot, isim))
if 50<= snot <=59:
    print("NOTUNUZ: CB {} {}".format(snot, isim))
if 40<= snot <=49:
    print("NOTUNUZ: CC {} {}".format(snot, isim))
if 0 <= snot <=39:
    print("NOTUNUZ: FF {} {}".format(snot, isim))




