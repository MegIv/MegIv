jarak_km = float(input('masukkan jarak tempuh (km): '))

harga = 0
if jarak_km < 0:
    print('Jarak tidak valid')
elif jarak_km <= 10:
    harga = 10000
elif 11 <= jarak_km <= 20:
    harga = 10000 + (jarak_km - 10) * 2500
elif 21 <= jarak_km <= 35:
    harga = 10000 + (10 * 2500) + (jarak_km - 20) * 1000
elif 36 <= jarak_km <= 40:
    harga = 50000
else:
    print('diluar jangkauan jarak tempuh')

print(f'biaya tranportasi adalah: {harga}')