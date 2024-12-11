s = 6

if not len(s) > 200:
    huruf_vokal = ['a', 'i', 'u', 'e', 'o']

    pasangan = []

    split_str = s.split(' ')
    jumlah_vokal = []

    for kata in split_str:
        jumlah = 0
        for huruf in kata:
            if huruf in huruf_vokal:
                jumlah += 1
        jumlah_vokal.append(jumlah)

    frekuensi = {}
    jumlah_fix_vokal = []

    for jumlah in jumlah_vokal:
        if jumlah in frekuensi:
            frekuensi[jumlah] += 1
        else:
            frekuensi[jumlah] = 1

    for jumlah in frekuensi:
        if frekuensi[jumlah] > 1:
            jumlah_fix_vokal.append(jumlah)

    for jumlah in jumlah_fix_vokal:
        for kata in split_str:
            count_vokal = 0
            for huruf in kata:
                if huruf in huruf_vokal:
                    count_vokal += 1
            if count_vokal == jumlah:
                pasangan.append(kata)

    print(pasangan)