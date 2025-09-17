class Main:
    def __init__(self):
        pass

    def main(self):
        pass

    def uiLogin(self):
        pass

    def uiMenu(self):
        pass

    def uiHitungPembayaran(self):
        pass

    def uiCetakStruk(self):
        pass


class LoginKasir:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def validasiLogin(self):
        pass

    def logout(self):
        pass


class KoneksiDatabase:
    def __init__(self, host: str, database: str, userName: str, password: str):
        self.host = host
        self.database = database
        self.userName = userName
        self.password = password

    def membukaKoneksi(self):
        pass

    def eksekusiQuerySelect(self):
        pass

    def eksekusiQueryInsert(self):
        pass

    def eksekusiQueryUpdate(self):
        pass

    def eksekusiQueryDelete(self):
        pass

    def tutupKoneksi(self):
        pass


class HitungPembayaran:
    def __init__(self, idMenu: str, namaMenu: str, harga: float, jumlah: int, totalHarga: float):
        self.idMenu = idMenu
        self.namaMenu = namaMenu
        self.harga = harga
        self.jumlah = jumlah
        self.totalHarga = totalHarga

    def insertPembayaran(self):
        pass

    def updatePembayaran(self):
        pass

    def deletePembayaran(self):
        pass

    def cariDataPembayaranByIdMenu(self):
        pass


class PembayaranTunai:
    def __init__(self):
        pass

    def hitungTotalHarga(self):
        pass


class PembayaranByCard:
    def __init__(self):
        pass

    def hitungTotalHarga(self):
        pass


class CetakStruk:
    def __init__(self):
        pass

    def cetakStruk(self):
        pass


class TcetakStruk:
    def __init__(self, noStruk: str, totalHarga: float):
        self.noStruk = noStruk
        self.totalHarga = totalHarga


class TabelHitungPembayaran:
    def __init__(self, idMenu: str, namaMenu: str, harga: float, jumlah: int, totalHarga: float):
        self.idMenu = idMenu
        self.namaMenu = namaMenu
        self.harga = harga
        self.jumlah = jumlah
        self.totalHarga = totalHarga

    def setIdMenu(self, idMenu: str):
        pass

    def getIdMenu(self):
        pass

    def setNamaMenu(self, namaMenu: str):
        pass

    def getNamaMenu(self):
        pass

    def setHarga(self, harga: float):
        pass

    def getHarga(self):
        pass

    def setJumlah(self, jumlah: int):
        pass

    def getJumlah(self):
        pass

    def setTotalHarga(self, totalHarga: float):
        pass

    def getTotalHarga(self):
        pass


class TabelPembayaranByCard:
    def __init__(self, idCard: str, jenisCard: str, namaBank: str, totalHarga: float):
        self.idCard = idCard
        self.jenisCard = jenisCard
        self.namaBank = namaBank
        self.totalHarga = totalHarga

    def setIdCard(self, idCard: str):
        pass

    def getIdCard(self):
        pass

    def setJenisCard(self, jenisCard: str):
        pass

    def getJenisCard(self):
        pass

    def setNamaBank(self, namaBank: str):
        pass

    def getNamaBank(self):
        pass

    def setTotalHarga(self, totalHarga: float):
        pass

    def getTotalHarga(self):
        pass
