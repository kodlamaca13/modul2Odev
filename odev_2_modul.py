
class Ogrenci:
    def __init__(self, ad,soyad,num):
        self.ad = ad
        self.soyad = soyad
        self.num = num

    def ogrenci_yaz(self):
        print("Ad:", self.ad)
        print("Soyad:", self.soyad)
        print("Num:", self.num)
        print("Not: Baki kalan bu kubbede, bir hoş sada imiş.")

"""_________1____________"""

def harf_frekansi_analizi(metin):
    metin = metin.lower()
    frekanslar = {}
    toplam_harf_sayisi = 0
    for karakter in metin:
        if karakter.isalpha():
            toplam_harf_sayisi += 1
            frekanslar[karakter] = frekanslar.get(karakter, 0) + 1
    return frekanslar, toplam_harf_sayisi

def metin_bolumleri_analiz_et(metin):
    bolumler = [100, 1000, 10000]
    for bolum in bolumler:
        kisim_metin = metin[:bolum]
        frekanslar, toplam_harf_sayisi = harf_frekansi_analizi(kisim_metin)
        print(f"{bolum} karakterlik bölümde harf frekansları:")
        for harf, frekans in frekanslar.items():
            yuzde = (frekans / toplam_harf_sayisi) * 100
            print(f"'{harf}' harfi {frekans} defa geçiyor ve metinde yüzde {yuzde:.2f} oranında bulunuyor.")
        print()

"""_______2_______"""

def kacinci_harf(metin3, sayi3):
    if sayi3 <= len(metin3):
        harf3 = metin3[sayi3 - 1]
        print(f"{sayi3}. harf: {harf3} sembolüdür.")
    else:
        print("Girdiğiniz sayı metin uzunluğunu aşıyor.")

"""_________3__________"""


def son_bas_harf_sil(metin4, adet4):
    if adet4 >= len(metin4):
        print("Hata: Silinecek harf adedi metnin uzunluğundan fazla olamaz.")
        return

    for i in range(adet4):
        if i % 2 == 0:  # Baştan silme
            print(f"{i + 1}. adımda baştaki '{metin4[0]}' harfi silindi.")
            metin4 = metin4[1:]
        else:  # Sondan silme
            print(f"{i + 1}. adımda sondaki '{metin4[-1]}' harfi silindi.")
            metin4 = metin4[:-1]

    print("Sonuç:", metin4)


"""_________4__________"""

def son_n_harf_basa_al(metin5, n5):
    if n5 >= len(metin5):
        print("Hata: Başa alınacak harf adedi metnin uzunluğundan fazla olamaz.")
        return

    son_harfler5 = metin5[-n5:]
    yeni_metin5 = son_harfler5 + " " + metin5[:-n5]
    print("Yeni metin:", yeni_metin5)



"""__________5_________"""

def son_n_harf_ters_cevir_yazdir(metin6, n6):
    son_ters6 = metin6[-1:-n6-1:-1]
    print(son_ters6)


"""____________6___________"""


