def count_the_stairs(n):
    if n == 0:
        return 1  # tidak perlu ambil langkah dari 0
    elif n == 1:
        return 1  # cuman 1 langkah, maka cuman 1 cara

    # meng-inisialisasikan sebuah array untuk menyimpan nilai/hasil perhitungannya
    # rekursif/dinamika pemrograman (dp)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


n = int(input())
print(count_the_stairs(n))