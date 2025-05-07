class karyawan:
    def salam(self):
        print(f"Halo, saya karyawan")

class manajer(karyawan):
    def salam(self):
        print(f"Halo, saya manajer")

k = karyawan()
k.salam()

m = manajer()
m.salam()

class karyawan1:
    def __init__(self,nama):
        self.nama = nama
    def salam(self):
        print(f"Haii {self.nama} saya adalah karyawan baru disini")

class manajer1(karyawan1):
    def salam(self):
        print(f"haii {self.nama} saya adalah manajer baru disini")

k1 = karyawan1("andii")
k1.salam()

m1 = manajer1("zakii")
m1.salam()