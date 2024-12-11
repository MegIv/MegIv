kategori = input('masukkan kode kategori : ')
harga = input('masukkan harga produk : ')

elektronik = 'E'
pakaian = 'P'
perabotan = 'F'


if kategori == 'E':
    print (f'Kategori produk {elektronik}')
    if harga >= 1000000:
        harga % 20
        print (harga)
    else:
        print(harga)
elif kategori == 'P':
    print(f'Kategori produk {pakaian}')
    if harga >= 500000:
        harga % 20
        print (harga)
    else:
        print(harga)

