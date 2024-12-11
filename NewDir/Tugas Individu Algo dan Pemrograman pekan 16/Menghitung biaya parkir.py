def hitung_biaya_parkir(durasi_parkir):
    # Tarif untuk 1 jam pertama
    tarif_pertama = 5000
    # Tarif untuk setiap jam setelah 1 jam pertama
    tarif_kedua = 3000

    if durasi_parkir <= 1:
        # Jika durasi parkir 1 jam atau kurang, biaya parkir hanya 5000
        total_biaya = tarif_pertama
    else:
        # Jika durasi parkir lebih dari 1 jam
        total_biaya = tarif_pertama + (durasi_parkir - 1) * tarif_kedua

    return total_biaya


# Input dari pengguna
durasi = float(input("Masukkan durasi parkir (dalam jam): "))

# Hitung biaya parkir
biaya = hitung_biaya_parkir(durasi)

# Tampilkan hasil
print(f"Biaya parkir untuk durasi {durasi} jam adalah Rp {biaya:,}")
