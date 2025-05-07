class laptop:
    merk = "asuss"
    harga = 8000000

laptop_saya = laptop()
print(laptop_saya.merk)
print(laptop_saya.harga)

class laptop:
    def __init__(self, merk, harga):
        self.merk = "asusss"
        self.harga = 8000000

    def info(self):
        print(f"saya punya laptop {self.merk}, harganya {self.harga}")
laptop_saya = laptop("lenovo",2000000)
laptop_saya.info()

    