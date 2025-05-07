class ayah:
        karakter = "lebih mentingkan ego nya"
        mindset = "mementingkan diri sendiri"
        rambut = "lurus"
        def sifat(self):
             print("sifat yang diwarisi ayahh")

class zaki(ayah):
    def sifat(self):
        print(f"sifat yang diwarisi ayah saya kepada saya rambut {self.rambut}")

ayahsaya = ayah()
ayahsaya.sifat()

saya = zaki()
saya.sifat()