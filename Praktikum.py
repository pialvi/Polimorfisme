#Pewarisan, polimerfisme
#ini adlah class utama
class FakultasTeknik:
	#construktor
    def __init__(self,Universitas, Fakultas, TahunAjar):
        self.univ = Universitas
        self.fak = Fakultas
        self.TA = TahunAjar

    #method atau function di class utama
    def CetakData(self):
        print('Universitas   : ',self.univ)
        print('Fakultas      : ',self.fak)
        print('Tahun Ajaran  : ',self.TA)
#ini adalah class turunan yang mewarisi sifat atau method dari class utama
class TeknikKomputer(FakultasTeknik):
	#construktor class utama yang di warisi ke kelas anak dengan manambahkan parameter baru
    def __init__(self,Universitas, Fakultas, TahunAjar, JumlahAngkatan):
        self.JA = JumlahAngkatan
        FakultasTeknik.__init__(self,Universitas, Fakultas, TahunAjar)
    def CetakData(self):
        print(2 * '@')
        print('Teknik Komputer')
        print('Universitas   : ', self.univ)
        print('Fakultas      : ', self.fak)
        print('Tahun Ajaran  : ', self.TA)
        print('Jumlah Angkatan di Prodi Teknik Komputer adalah', self.JA)
        print(2 * '@')

class PTIK(FakultasTeknik):
    def __init__(self, Universitas, Fakultas, TahunAjar, JumlahAngkatan, Jurusan):
        self.JA = JumlahAngkatan
        self.J = Jurusan
        FakultasTeknik.__init__(self, Universitas, Fakultas, TahunAjar)

    def CetakData(self):
        print('Pendidikan Teknik Informatika & Komputer')
        print('Universitas   : ', self.univ)
        print('Fakultas      : ', self.fak)
        print('Jurusan      : ', self.J)
        print('Tahun Ajaran  : ', self.TA)
        print('Jumlah Angkatan di Prodi Teknik Informatika & Komputer adalah', self.JA)
        print(15 * '@')
class Mekatronika(FakultasTeknik):
    def __init__(self, Universitas, Fakultas, TahunAjar, JumlahAngkatan):
        self.JA = JumlahAngkatan
        FakultasTeknik.__init__(self, Universitas, Fakultas, TahunAjar)

    def CetakData(self):
        print('Pendidikan Vokasi Mekatronika')
        print('Universitas   : ', self.univ)
        print('Fakultas      : ', self.fak)
        print('Tahun Ajaran  : ', self.TA)
        print('Jumlah Angkatan di Prodi Pendidikan Vokasi Mekatronika adalah', self.JA)
        print(2 * '@')

def main():
	#deklarasi objek
    a = FakultasTeknik('Universitas Negeri Makassar', 'Teknik', 2018 )
    a.CetakData()


    #penghapusan objek
    del a
     #,e,buat objek baru yang sama  dengan class yang berbeda
    a = TeknikKomputer('Universitas Negeri Makassar', 'Teknik', 2018, 2 )
    a.CetakData()

    b = PTIK('Universitas Negeri Makassar', 'Teknik', 2018, 15, 'Pendidikan Teknik Elektro & Pendidikan Teknik Elektronika')
    b.CetakData()

    del b

    b = Mekatronika('UNM', 'Teknik', 2018, 2)
    b.CetakData()



if __name__ == "__main__":
    main()
