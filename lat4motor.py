class motor:
    merk = "alva"
    warna = "hitam"
    tipe = "motor listrik"
    tipe_bahan_bakar = "fixed battery"
motor_saya = motor()
print(motor_saya.merk) ## output alva
print(motor_saya.warna) ## output hitam
print(motor_saya.tipe) ## output motor listrik 
print(motor_saya.tipe_bahan_bakar) ## output fixed battery

class motor:
    def __init__(self):
        self.merk = "alva"
        self.warna = "hitam"
        self.tipe = "motor listrik"
    def jalan(self):
        print("motor maju")
    def berhenti(self):
        print("motor berhenti")
    def lampusenkanan(self):
        print("motor lampu sen kanan")
    def lampusenkiri(self):
        print("motor lampu sen kiri")
motorA = motor()
motorB = motor()
motorC = motor()

motorA.jalan()
motorB.berhenti()
motorC.lampusenkanan()