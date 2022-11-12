import time
print("UYGULAMAYI SONLANDIRMAK İÇİN çıkış / ÇIKIŞ yazınız.")
print("UYGULAMALARDA GEZİNMEK İÇİN ÖNCELİKLE UYGULAMA AÇMANIZ GEREKİYOR")

class bilgisayar():

    def __init__(self,durum="kapalı",ses_ayar=0,anasayfa=["ana sayfa","spotify","google"],komut="arama yeri",uygulamalar=["google","spotify"]):
        self.durum=durum
        self.ses_ayar=ses_ayar
        self.anasayfa=anasayfa
        self.komut=komut
        self.uygulamalar=uygulamalar

    def pc_ac(self):
        if self.durum=="açık":
            print("bilgisayar zaten açık")
        else:
            print("bilgisayar açılıyor..")
            time.sleep(0.2)
            self.durum="açık"
    def pc_kapa(self):
        if self.durum=="kapalı":
            print("bilgisayar zaten kapalı")
        else:
            print("bilgisayarınız kapanıyor..")
            time.sleep(0.2)
            self.durum="kapalı"

    def ses_ac_kıs(self):
        while True:
            sesaç=input("> ses yükseltir, < ses kısar \n kaydedip çıkmak için 'q' tuşuna basın")
            if sesaç==">":
                if self.ses_ayar>=0:
                    self.ses_ayar+=1
                    print(self.ses_ayar)
            elif sesaç=="<":
                if not self.ses_ayar==0:
                    self.ses_ayar-=1
                print(self.ses_ayar)
            elif sesaç=="q":
                print("güncel ses: ",self.ses_ayar)
                break
            else:
                print("geçersiz işlem")
                break
    def zaten_anasayfa(self):
        if self.anasayfa=="ana sayfa":
            print("zaten ana sayfadasınız")
    def ana_sayfa(self):
        if self.anasayfa=="google":
            print("ana sayfaya geçiliyor..")
            self.anasayfa="ana sayfa"
            print("ana sayfaya geçiş yapıldı...")
        elif self.anasayfa=="spotify":
            print("ana sayfaya geçiş yapılıyor..")
            self.anasayfa="ana sayfa"
            print("ana sayfaya geçiş yapıldı..")
        else:
            print("zaten ana sayfadasınız")
    def uygulamalarx(self):

        soru=input("hangi işlemi yapmak istiyorsunuz :\n uygulamaya girmek için : 1    \nuygulamaları görmek için: 2 \n  ")
        if soru=="1":
            uyg_soru=input("hangi uygulamaya girmek istiyorsunuz.?:   ")
            if uyg_soru=="spotify":
                print("spotify uygulamasına giriş yaptınız")
                self.anasayfa="spotify"
            elif uyg_soru=="google":
                print("google uygulamasına giriş yaptınız")
                self.anasayfa="google"
        elif soru=="2":
                print(self.uygulamalar)
    def komutx(self):

        print("şuanda arama kısmındasınız")
        print("burada bu bilgisayar programındaki şeyleri aratabilirsiniz")
        print("belirli komutlar vardır bunlar şunlardır:\n bilgisayarı kapatmak için: kapat\n bilgisayarı açmak için: aç\n sesi açmak için veya kısmak için: ses\n ana sayfaya gelmek için ana sayfa\n uygulama açmak ve gezinmek için uygulamalar yazmanız gerek")
        arat=input("ara: ")
        if arat=="kapat":
            bilgisayar1.pc_kapa()
        elif arat=="aç":
            bilgisayar1.pc_ac()
        elif arat=="ses":
            bilgisayar1.ses_ac_kıs()
        elif arat=="ana sayfa":
            bilgisayar1.ana_sayfa()
        elif arat=="uygulamalar":
            self.uygulamalarx()


bilgisayar1=bilgisayar()


print("""Bilgisayar Uygulaması
Bilgisayarı Açmak İçin : 1
Bilgisayarı Kapatmak İçin : 2
Bilgisayarın Sesini Ayarlamak İçin: 3
Bilgisayarda Ana Sayfaya Gitmek İçin : 4
Bilgisayarda Uygulama Değiştirmek İçin: 5
Bilgisayarda Komut İşlemi Yapmak için : 6

""")

while True:
    işlem=input("İşleminizi Seçin")
    if işlem=="1":
        bilgisayar1.pc_ac()
    elif işlem=="2":
        bilgisayar1.pc_kapa()
    elif işlem=="3":
        print("güncel ses: ",bilgisayar1.ses_ayar)
        bilgisayar1.ses_ac_kıs()
    elif işlem=="4":
        bilgisayar1.ana_sayfa()
    elif işlem=="5":
        bilgisayar1.uygulamalarx()
    elif işlem=="6":
        bilgisayar1.komutx()
    elif işlem=="q":
        break
    else:
        print("geçersiz işlem")

