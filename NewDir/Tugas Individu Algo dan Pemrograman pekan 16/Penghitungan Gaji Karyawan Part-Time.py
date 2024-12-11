def hitung_gaji_karyawan():
    # Input nama karyawan
    nama_karyawan = input("Masukkan nama karyawan: ")

    # Input tarif per jam normal
    tarif_normal = float(input(f"Masukkan tarif per jam {nama_karyawan}: "))

    # Input total jam kerja karyawan dalam sebulan
    jam_kerja_sebulan = int(input("Masukkan total jam kerja karyawan dalam sebulan: "))

    # Input jumlah jam kerja pada weekend (Sabtu/Minggu)
    jam_weekend = int(input("Masukkan jumlah jam kerja pada weekend (Sabtu/Minggu): "))

    # Menghitung jam kerja biasa (selain weekend)
    jam_biasa = jam_kerja_sebulan - jam_weekend

    # Menghitung gaji untuk jam kerja biasa dan weekend
    gaji_normal = tarif_normal * jam_biasa
    gaji_weekend = tarif_normal * 1.5 * jam_weekend

    # Menghitung total gaji tanpa bonus
    total_gaji = gaji_normal + gaji_weekend

    # Menghitung bonus
    if jam_kerja_sebulan > 150:
        bonus = 500000
    elif jam_kerja_sebulan > 100:
        bonus = 200000
    else:
        bonus = 0

    # Menambahkan bonus ke total gaji
    total_gaji += bonus

    # Menampilkan hasil
    print(f"\nGaji untuk {nama_karyawan}:")
    print(f"Gaji tanpa bonus: Rp {total_gaji - bonus:.2f}")
    print(f"Bonus: Rp {bonus:.2f}")
    print(f"Total gaji {nama_karyawan}: Rp {total_gaji:.2f}")


# Menjalankan fungsi
hitung_gaji_karyawan()
