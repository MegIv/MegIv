n = input()

if n[0] != ' ' and n[-1] != ' ':
    split_n = n.split()

    bil_ganjil = 0
    bil_genap = 0

    for i in split_n:
        angka = int(i)
        if angka % 2 == 0:
            bil_genap += 1
        else:
            bil_ganjil += 1

print(bil_genap)
print(bil_ganjil)