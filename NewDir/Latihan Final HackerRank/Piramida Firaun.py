n = int(input())

if n % 2 == 1:
    for i in range(1, n+1, 2):
        print(' ' * (n-i) +'* ' * i)
    for i in range(n-2, 0 , -2):
        print(' ' * (n-i) + '* ' * i)
else:
    for i in range(1, n, 2):
        print(' ' * (n-i) + '* ' * i)
    for i in range(n-1, 0, -2):
        print(' ' * (n-i) + '* ' * i)