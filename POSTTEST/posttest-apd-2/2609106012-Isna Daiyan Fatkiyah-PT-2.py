Barang_1 = 15000
Barang_2 = 25000
Barang_3 = 10000
Barang_4 = 5500
Barang_5 = 5000
Barang_6 = 20000
NIM = 12

Barang = [Barang_1, Barang_2, Barang_3, Barang_4, Barang_5, Barang_6]

Total_Belanjaan = Barang_1 + Barang_2 + Barang_3 + Barang_4 + Barang_5 + Barang_6

Pajak = 0.15 * Total_Belanjaan

Total_Bayar = Total_Belanjaan + Pajak

Rata_Rata = Total_Belanjaan / len(Barang)

Bolean = (NIM) < int(Rata_Rata)
print(Bolean)
print(Rata_Rata)
print(NIM)
