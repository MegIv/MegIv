nilai_mahasiswa = [55,78,82,67,90,58,74]
jumlah_lebih_70 = 0

for nilai in nilai_mahasiswa:
    if nilai > 70:
        jumlah_lebih_70 += 1

total_nilai = sum(nilai_mahasiswa)
print('total nilainya adalah : ',total_nilai)
banyak_nilai = len(nilai_mahasiswa)
print('banyak nilai adalah : ',banyak_nilai)
rata2 = total_nilai/banyak_nilai

print(f'rata-rata nilai adalah : ' ,{rata2} )