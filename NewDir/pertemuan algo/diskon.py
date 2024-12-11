n = int(input("berapa barang :"))
x = []
y = []
for _ in range (n):
    a = input("nama barang : ")
    b = int(input("harga barang: "))
    x.append(a)
    y.append(b)

if n == 2 :
    total = max(y)+min(y)*0.9
    print(total)
elif n > 2 :
    total = min(y)*0.9
    nodiskon = sum(y) - min(y) +total
    result = nodiskon*0.95
    print(result)