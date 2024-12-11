def hitung_rata_rata_dan_status_kelulusan():
    # Input jumlah siswa
    jumlah_siswa = int(input("Masukkan jumlah siswa: "))

    # Loop untuk menghitung rata-rata nilai dan kelulusan per siswa
    for i in range(jumlah_siswa):
        print(f"\nMasukkan nilai untuk Siswa ke-{i + 1}:")

        # Input jumlah nilai ujian
        jumlah_nilai = int(input("Masukkan jumlah nilai ujian: "))

        # List untuk menyimpan nilai ujian siswa
        nilai_ujian = []

        # Input nilai ujian satu per satu
        for j in range(jumlah_nilai):
            nilai = float(input(f"Masukkan nilai ujian ke-{j + 1}: "))
            nilai_ujian.append(nilai)

        # Menghitung rata-rata nilai
        rata_rata = sum(nilai_ujian) / len(nilai_ujian)

        # Menentukan status kelulusan
        if rata_rata >= 80:
            status = "Lulus dengan Predikat A"
        elif rata_rata >= 70:
            status = "Lulus dengan Predikat B"
        elif rata_rata >= 60:
            status = "Lulus dengan Predikat C"
        else:
            status = "Tidak Lulus"

        # Menampilkan hasil
        print(f"\nRata-rata nilai siswa ke-{i + 1}: {rata_rata:.2f}")
        print(f"Status kelulusan: {status}")


# Menjalankan fungsi
hitung_rata_rata_dan_status_kelulusan()