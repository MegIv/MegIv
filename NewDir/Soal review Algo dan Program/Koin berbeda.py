baris_koin = input('masukkan baris karakter jenis koin: ')

frekuensi = {}
for koin in baris_koin:
    if koin in frekuensi:
        frekuensi[koin] += 1
    else:
        frekuensi[koin] = 1

koin_berbeda = ''
for koin in frekuensi:
    if frekuensi[koin] == 1:
        koin_berbeda = koin
        break

posisi_koin = baris_koin.index(koin_berbeda) + 1
print(posisi_koin)