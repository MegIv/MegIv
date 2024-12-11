def hitung_total_belanja():
    # Input untuk uang yang dimiliki
    uang = float(input("Masukkan jumlah uang yang dimiliki Bu Cila: "))

    # List untuk menyimpan harga barang yang dibeli
    harga_barang = []

    # Input jumlah barang yang dibeli
    jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))

    # Input harga barang satu per satu
    for i in range(jumlah_barang):
        harga = float(input(f"Masukkan harga barang ke-{i + 1}: "))
        harga_barang.append(harga)

    # Menghitung total belanja
    total_belanja = sum(harga_barang)

    # Menampilkan total belanja
    print(f"Total belanja Bu Cila: Rp {total_belanja:.2f}")

    # Memeriksa apakah uang cukup
    if uang >= total_belanja:
        sisa_saldo = uang - total_belanja
        print(f"Uang cukup. Sisa saldo Bu Cila: Rp {sisa_saldo:.2f}")
    else:
        kekurangan = total_belanja - uang
        print(f"Uang tidak cukup. Kekurangan: Rp {kekurangan:.2f}")


# Menjalankan fungsi
hitung_total_belanja()
# def total_belanja():
#     uang = float(input('masukkan jumlah uang ibu cila: '))
#
#     while True:
#        harga_barang = float(input('masukkan harga barang'))