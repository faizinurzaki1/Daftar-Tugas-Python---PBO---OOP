class siswa:
    def __init__(self,nama,nim,jurusan):
        self.nama = "zakii"
        self.nim = 123456678
        self.jurusan = "rekayasa perangkat lunak"
    
    def info(self):
        print("nama:", self.nama)
        print("nim:", self.nim)
        print("jurusan:", self.jurusan)
saya = siswa("zaki", 12345678 , "rekayasa perangkat lunak")
saya.info()