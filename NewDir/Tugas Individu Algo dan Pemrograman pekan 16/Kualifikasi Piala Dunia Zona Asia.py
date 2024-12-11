jumlah_tim = int(input("Masukkan jumlah tim: "))
print("Masukkan data tim berturut-turut yang dibatasi spasi: ")
print("(Format: NamaTim main menang seri kalah JumlahGol GolKebobolan)")

result = []

for tim in range(jumlah_tim):
    data_tim = input()

    poin = 0
    split_data = data_tim.split()

    nama_tim = split_data[0]
    main = split_data[1]
    menang = int(split_data[2])
    seri = int(split_data[3])
    kalah = split_data[4]
    jumlah_gol = int(split_data[5])
    gol_kebobolan = int(split_data[6])

    poin += menang * 3 + seri * 1
    selisih_gol = jumlah_gol - gol_kebobolan

    result.append({
        "nama_tim": nama_tim,
        "poin": poin,
        "selisih_gol": selisih_gol,
    })

tim_terurut = sorted(result, key=lambda tim: (tim['poin'], tim['selisih_gol']), reverse=True)

for idx, tim in enumerate(tim_terurut, start=1):
    status = ""
    if idx <= 2:
        status = "Lolos Otomatis"
    elif idx == 3 or idx == 4:
        status = "Play-Off"
    elif idx >= 5:
        status = "Gugur"

    print(f"{idx}. {tim['nama_tim']} {tim['poin']} Poin (Selisih Gol: {tim['selisih_gol']}) [{status}]")