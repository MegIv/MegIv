n = int(input())

angka = ""

stringTerpanjang = ""

for idx in range(1, n + 1):
    stringTerpanjang += str(idx)

spasiTambahan = 0

if 0 <= n <= 1000000:
    for i in range(1, n + 1):
        if len(str(i)) > 1:
            spasiTambahan += 1
        spasiDikurangi = (len(stringTerpanjang) - i) - spasiTambahan
        spasi = spasiDikurangi * " "
        for j in range(i, i + 1):
            angka += str(j)
        print(f"{spasi}{angka}")