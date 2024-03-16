def collatz_hesapla(x):
    while x != 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        print(x)


baslangic_sayisi = int(input("Başlangıç sayısını girin: "))


collatz_hesapla(baslangic_sayisi)
