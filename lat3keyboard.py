class keyboard:
    def __init__(self,):
        self.merk = "lenovo"
        self.warna = "hitam"
        self.tipe = "qwerty"

keyboard_saya = keyboard()
print(keyboard_saya.merk)
print(keyboard_saya.warna) 
print(keyboard_saya.tipe)

class keyboard:
    def __init__(self):
        self.merk = "lenovo"
        self.warna = "hitam"
        self.tipe = "qwerty"

    def mengetik(self):
        print("untuk mengetik")
    def main(self):
        print("bermain game")
   
keyboard1 = keyboard()
keyboard2 = keyboard()


keyboard1.mengetik()
keyboard2.main()
