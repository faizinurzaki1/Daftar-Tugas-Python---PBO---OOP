class rekeningbank:
    def __init__(self,saldo):
        self.__saldo = saldo 
    def lihatsaldo(self):
        print(f"saldo anda {self.__saldo} rupiah")
    def tambah_saldo(self, jumlah):
        self.__saldo += jumlah
        print(f"saldo anda ditambahkan {jumlah} ")
    def tarik_saldo(self,jumlah):
        self.__saldo -= jumlah
        print(f"saldo anda ditarik sebesar {jumlah} ")

rb = rekeningbank(0)
rb.lihatsaldo()
rb.tambah_saldo(100000)
rb.tarik_saldo(5000)
rb.lihatsaldo()