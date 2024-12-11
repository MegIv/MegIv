n = int(input())
m = int(input())

genap = []

for i in range(n, m + 1, 1):
    if i % 2 == 0:
        genap.append(i)

hasil = sum(genap)
print(hasil)