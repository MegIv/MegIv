benar = int(input("Masukkan jumlah soal benar: "))
salah = int(input("Masukkan jumlah soal salah: "))
tidak_dijawab = 50 - (benar+salah)
t_soal = benar+salah

n_benar = benar*5
n_salah = salah*(-3)
n_tj = tidak_dijawab * 0
t_nilai = n_benar+n_salah+n_tj

if t_soal > 50:
    print(f"Total nilai {t_nilai}")
    print(f"Total soal yang dijawab {t_soal}")
    print("Jumlah soal tidak valid. Soal hanya berjumlah 50 soal.")
elif tidak_dijawab == 50:
    print(f"Total nilai {t_nilai}")
    print(f"Total soal yang dijawab {t_soal}")
    print("Peserta didiskualifikasi. Tidak ada soal yang dijawab.")
else:
    if t_nilai > 100:
        print(f"Total nilai {t_nilai}")
        print(f"Total soal yang dijawab {t_soal}")
        print("Lolos ke tahap selanjutnya.")
    else:
        print(f"Total nilai {t_nilai}")
        print(f"Total soal yang dijawab {t_soal}")
        print("Peserta dinyatakan gugur.")