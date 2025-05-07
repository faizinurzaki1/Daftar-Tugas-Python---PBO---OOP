class Nilaisiswa:
    def __init__(self,nama,nilaiujian):
        self.__nama = nama
        self.__nilaiujian = nilaiujian

    def info(self):
        print(f"siswa,{self.__nama},mendapatkan {self.__nilaiujian}")
    def ubahnilai(self, nilai_baru):
        if 0 <= nilai_baru <= 100:
            self.__nilaiujian = nilai_baru
            print("nilai harus di ubah")
        else:
            print("nilai harus antara 0 - 100")
        def get_nama(self):
            return self.__nama
        def get_nilai(self):
            return self.__nilaiujian
siswa = Nilaisiswa("jaki", 90)
siswa.info()
siswa.ubahnilai(99)
siswa.info()
siswa.ubahnilai(110)
print(siswa.get_nama())
print(siswa.get_nilai())