class Produk:
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    def tampilkan_info(self):
        total = self.hitung_total()
        print(f"{self.nama} - Rp{self.harga:,} x {self.jumlah} = Rp{total:,}")

    def hitung_total(self):
        return self.harga * self.jumlah

    def hitung_diskon(self, total_semua):
        if total_semua > 5000000:
            return total_semua * 0.05
        return 0