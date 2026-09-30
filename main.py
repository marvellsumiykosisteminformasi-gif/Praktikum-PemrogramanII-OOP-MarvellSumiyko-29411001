from Produk import Produk

jumlah_produk = int(input("Masukkan jumlah produk yang dibeli: "))

daftar_produk = []

for i in range(jumlah_produk):
    print(f"\nProduk ke-{i + 1}")

    nama = input("Nama produk  : ")
    harga = int(input("Harga produk : Rp"))
    jumlah = int(input("Jumlah beli  : "))

    produk = Produk(nama, harga, jumlah)
    daftar_produk.append(produk)

print("\n=== DETAIL PEMBELIAN ===")

total_semua = 0

for produk in daftar_produk:
    produk.tampilkan_info()
    total_semua += produk.hitung_total()

produk_terakhir = daftar_produk[-1]
diskon = produk_terakhir.hitung_diskon(total_semua)

total_bayar = total_semua - diskon

print("\n=== HASIL PEMBELIAN ===")
print(f"Total Pembelian : Rp{total_semua:,.0f}")
print(f"Diskon 5%       : Rp{diskon:,.0f}")
print(f"Total Bayar     : Rp{total_bayar:,.0f}")