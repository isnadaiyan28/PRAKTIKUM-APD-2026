nama_pembeli = input("masukkan nama anda: ")
umur_pembeli = int(input("masukkan umur anda: "))

if umur_pembeli < 13:
    print("Mohon maaf, anda belum cukup umur untuk menonton")
else:
    jenis_tiket = input("masukkan jenis tiket (Reguler/Premium/VIP): ").lower()
    if jenis_tiket == "reguler":
        harga_tiket = 50000
        print("Harga tiket Reguler adalah Rp50.000")
    elif jenis_tiket == "premium":
        harga_tiket = 75000
        print("Harga tiket premium adalah Rp75.000")
    else: 
        harga_tiket = 100000
        print("Harga tiket VIP adalah Rp100.000")

    status_member = input("Apakah anda adalah member (ya/tidak): ").lower()

    status_member = "ya"
    diskon = harga_tiket * 0.2
    total_bayar = harga_tiket - diskon
    diskon = "Anda mendapatkan diskon 20% untuk pembelian tiket" if status_member == "ya" else "Anda tidak akan mendapatkan diskon untuk pembelian tiket"
    print(f"total yang harus anda bayar adalah: Rp{total_bayar if status_member == "ya" else harga_tiket}")
