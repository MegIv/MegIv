# def belajar():
#     # print('selamat belajar')
#
# belajar()

# def belajar (a, b):
#     c = a + b
#     return 'yuhu hu

# nilai_tugas = int(input('nilai tugas '))
# nilai_kuis = int(input('nilai kuis '))
# nilai_uts = int(input('nilai uts '))
# nilai_uas = int(input('nilai uas '))

# def penilaian ():
#     tugas = nilai_tugas * 0.80
#     print(tugas)
#
#     kuis = nilai_kuis * 0.90
#     print(kuis)
#
#     uts = nilai_uts * 0.70
#     print(uts)
#
#     uas = nilai_uas * 0.60
#     print(uas)
#
#
#
# print(penilaian())

'''meghitung max min rata rata nilai'''
# def menghitung (*a):
#     maximum = max(a)
#     minimum = min(a)
#     b = sum(a)
#     # b = 0
#     # for i in a :
#     #     b += i
#     mean = b/len(a)
#     return maximum, minimum, mean
# a = int(input('Masukkan nilai a '))
# b = int(input('Masukkan nilai b '))
# c = int(input('Masukkan nilai c '))
# max, min, mean = menghitung(a, b ,c)
# print(max)
# print(min)
# print(mean)

'''fungsi rekrusif'''
# def show_interview (star, end):
#     print(star)
#     star += 1
#     if star <= end :
#         show_interview(star, end)
# show_interview(1,10)
#
'''persamaan operasi/fungsi'''
# star = 1
# while star <= 10 :
#     print(star)
#     star += 1

'''faktorial'''
def faktorial(n):
    if n == 1:
        return
    else:
        return n * faktorial(n-1)
    