gsayı = int(input("Bir sayı giriniz:"))
def tambölen(sayı):
    a = []
    for i in range(1,gsayı):
        if gsayı % i == 0:
            a.append(i)
    return a
print(tambölen(gsayı))