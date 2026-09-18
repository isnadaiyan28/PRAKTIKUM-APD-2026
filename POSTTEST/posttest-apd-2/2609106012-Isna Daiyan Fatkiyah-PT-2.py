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

bolean = NIM < Rata_Rata

Total_Bayar_Baht = Total_Bayar / 533.8582
Total_Bayar_Won = Total_Bayar / 12.8243

print ("Harga Barang yang Dibeli (Barang 1)               : Rp", Barang_1)
print ("Harga Barang yang Dibeli (Barang 2)               : Rp", Barang_2)
print ("Harga Barang yang Dibeli (Barang 3)               : Rp", Barang_3)
print ("Harga Barang yang Dibeli (Barang 4)               : Rp", Barang_4)
print ("Harga Barang yang Dibeli (Barang 5)               : Rp", Barang_5)
print ("Harga Barang yang Dibeli (Barang 6)               : Rp", Barang_6)
print ("Total Belanjaan                                   : Rp", Total_Belanjaan)
print ("Pajak 15%                                         : Rp", Pajak)
print ("Total Bayar                                       : Rp", Total_Bayar)
print ("Rata-rata Belanjaan                               : Rp", Rata_Rata)
print ("Total Bayar dalam Baht                            : ฿", Total_Bayar_Baht)
print ("Total Bayar dalam Won                             : ₩", Total_Bayar_Won)
print ("NIM (2 digit terakhir NIM)                        :", NIM)
print ("Bolean (NIM < Rata-rata)                          :", bolean)
print ("Harga barang 1, Barang 3, dan Barang 5            : Rp",Barang[0:5:2])

