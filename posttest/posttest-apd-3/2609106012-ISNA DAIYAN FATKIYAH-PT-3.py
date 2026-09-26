print("=" * 40)
print("     selamat datang di bioskop kami")
print("=" * 40)

nama_pembeli = input("Silahkan masukkan nama anda: ")
umur_pembeli = int(input("Silahkan masukkan umur anda: "))

if umur_pembeli < 13:
    print("Mohon maaf, anda belum cukup umur untuk menonton")
else:
    print("Anda cukup umur untuk dapat menonoton, silahkan pilih jenis tiket yang tersedia")

    print("-----pilihan jenis tiket-----")
    print("1. Reguler : Rp50.000")
    print("2. Premium : Rp75.000")
    print("3. VIP     : Rp100.000")
    jenis_tiket = input("masukkan jenis tiket (Reguler/Premium/VIP): ").lower()
  
    if jenis_tiket == "reguler" or jenis_tiket == "1":
        harga_tiket = 50000
        jenis_tiket = "Reguler"
    elif jenis_tiket == "premium" or jenis_tiket == "2":
        harga_tiket = 75000
        jenis_tiket = "Premium"
    elif jenis_tiket == "vip" or jenis_tiket == "3": 
        harga_tiket = 100000
        jenis_tiket = "VIP"
    else:
        harga_tiket = 0

    if harga_tiket == 0:
        print("jenis tiket yang anda masukkan tidak tersedia, transaksi dibatalkan")
    else:

        status_member = input("Apakah anda adalah member (ya/tidak): ").lower()

        diskon = harga_tiket * 0.2 if status_member == "ya" else 0
        total_bayar_sementara = harga_tiket - diskon

        biaya_admin = 0 if status_member == "ya" else 2000   
        total_bayar = total_bayar_sementara + biaya_admin 
        print("\n" + "total yang harus anda bayarkan adalah : Rp", total_bayar)  

        bayar = int(input("masukkan jumlah uang yang dibayarkan: Rp"))
        if bayar < total_bayar:
            print("uang yang anda bayarkan kurang, transaksi dibatalkan")
        else:
            if bayar > total_bayar:
                kembalian = bayar - total_bayar
            else:
                kembalian = 0

            print("\n" + "=" * 40)
            print("            STRUK PEMBELIAN")
            print("=" * 40)
            print("Nama pembeli          : ", nama_pembeli)
            print("Umur pembeli          : ", umur_pembeli)
            print("Jenis tiket           : ", jenis_tiket)
            print("Status Member         : ", status_member)
            print("-" * 40)
            print("Harga tiket           : Rp", harga_tiket)
            print("Diskon member         : Rp", diskon)
            print("Biaya admin           : Rp", biaya_admin)
            print("-" * 40)
            print("Total bayar           : Rp", total_bayar)
            print("Uang bayar            : Rp", bayar )
            print("Kembalian             : Rp", kembalian)
            print("=" * 40)