n, m, r = int(input()), list(map(int, input().split())), True

primas = [x for x in range(2, n + 1) if all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))]

for i in range(len(m)):
    for j in range(i + 1, len(m)):
        if m[i] + m[j] in primas:
            print(f'({m[i]}, {m[j]})')
            r = False

print('Tidak ada pasangan yang ditemukan') if r else ''