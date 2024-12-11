n = int(input())
m = int(input())

kata = ''
count = 0

for i in range(n, m + 1):
    kata += str(i) + ', '
    count += 1
    if count == 5:
        kata += '\n'
        count = 0

print(kata)