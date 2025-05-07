class hewan:
    def __init__(self,nama):
        self.nama = nama
    def suara(self):
        print("hewan bersuara")
class kucing(hewan):
    def suara(self):
        print(f"{self.nama} meonggg")

class domba(hewan):
    def suara(self):
        print(f"{self.nama} mbeee")

class sapi(hewan):
    def suara(self):
        print(f"{self.nama} moooo")
h = hewan("hewan umum")
h.suara()

k = kucing("kucing")
k.suara()

b = domba("domba")
b.suara()

s = sapi("sapi")
s.suara()