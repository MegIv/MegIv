n = int(input())
list_angka = input()

split_list = list_angka.split()

digit = 0
more_6_digit = False

for temp in split_list:
    if len(temp) > 6:
        more_6_digit = True

if len(split_list) == n and 1 <= n <= 100 and not more_6_digit:
    for angka in split_list:
        digit += len(angka)

    print(digit)