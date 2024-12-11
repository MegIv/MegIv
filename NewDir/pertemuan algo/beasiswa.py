lolos = True
alasanTidakLolos = []

nilaiAkademik = int(input("Masukkan Nilai Akademik : "))
jumlahKegiatan = int(input("Masukkan jumlah kegiatan ekstrakurikuler yang diikuti : "))
for i in range(1, jumlahKegiatan + 1):
    nilaiKegiatan = int(input(f"Masukkan nilai keaktifan kegiatan-{i} : "))
    if nilaiKegiatan < 70:
        lolos = False
        alasanTidakLolos.append(f"Nilai keaktifan kegiatan-{i} tidak lolos")
pendapatan = int(input("Masukkan Pendapatan : "))
nilaiWawancara = int(input("Masukkan nilai wawancara : "))

if nilaiAkademik < 85:
    lolos = False
    alasanTidakLolos.append("Nilai akademik kurang dari 85")

if pendapatan > 3000:
    lolos = False
    alasanTidakLolos.append("Pendapatan lebih dari 3000")

if jumlahKegiatan < 3:
    lolos = False
    alasanTidakLolos.append("Jumlah kegiatan kurang dari 3")

if nilaiWawancara < 75:
    lolos = False
    alasanTidakLolos.append("Nilai wawancara kurang dari 75")

if lolos:
    print("Lolos Beasiswa")
else:
    print(f"Tidak Lolos Beasiswa")
    print("Alasan Tidak Lolos: ")
    for alasan in alasanTidakLolos:
        print(alasan)