
def hitung_rata_rata_dan_status_kelulusan():
    # Input jumlah nilai ujian
    jumlah_nilai = int(input("Masukkan jumlah nilai ujian: "))

    # List untuk menyimpan nilai ujian
    nilai_ujian = []

    # Input nilai ujian satu per satu
    for i in range(jumlah_nilai):
        nilai = float(input(f"Masukkan nilai ujian ke-{i + 1}: "))
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
    print(f"\nRata-rata nilai: {rata_rata:.2f}")
    print(f"Status kelulusan: {status}")


# Menjalankan fungsi
hitung_rata_rata_dan_status_kelulusan()