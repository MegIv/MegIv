# x = 'aku'
# y = 'sigma'
#
#
# print(x + y)
#
#
# x = 'aku'
# y = 'sigma'
#
#
# print(x + ' ' + y)
#
# x = 'aku'
# y = 'sigma'
#
#
# for i in x:
#     print(i)
#
# x = 'aku'
# y = 'sigma'
#
#
# print(len(y))
#
# x = 'aku'
# y = 'sigmasigma'
#
#
# print(y.count('sig'))
#
# x = 'aku'
# y = 'sigma   sigma'
#
# print(y.count(' '))
#
# '''index mulai dari 1'''
# x = 'aku'
# z = 'sistem informasi'
# y = 'sigmasigma'
#
#
# print(z[5])
#
# x = 'aku'
# z = 'sistem informasi 2024 departemen Matematika Fakultas MIPA'
# y = 'sigmasigma'
#
#
# print(z[7:16])
# #mirip dengan looping for
# print(z[:7])
# print(z[0:16:2])
# #dari belakang
# print(z[-14:])
# #jalan ke kiri
# print(z[::-1])
# #jalan ke kanan
# print(z[::1])
# print(z[0::1])
#
# x = 'aku'
# z = 'sistem informasi 2024 departemen Matematika Fakultas MIPA'
# y = 'sigmasigma'
#
#
# print(z.startswith('informasi'))
# print(z.endswith('MIPA'))
# print(z.startswith('s'))
#
# for i in range(5):
#     print(y, end=' ')
#
# x = 'aku'
# z = 'sistem informasi 2024 departemen Matematika Fakultas MIPA'
# y = 'sigmasigma'
#
# #buat ganti kalimatnya
# print(z.replace("MIPA", "Teknik"))
# #buat upper case
# print(z.upper())
# #buat lower case
# print(z.lower())
# #buat capitalize each word
# print(z.title())
# #buat capitalize pertama saja
# print(z.capitalize())
# #hari keterbalikan
# print(z.swapcase())
#
# x = 'aku'
# z = 'sistem informasi 2024 departemen Matematika Fakultas MIPA'
# y = 'sigma-sigma'
# a = [x, z, y]
# #fyi .join buat array
# print('-'.join(a))
# print(y.split('-'))
#
# s1 = 'Abc'
# s2 = 'Xyz'
# s2_2 = s2[::-1]
#
# for i in range(len(s2_2)):
#     print(s1[i] + s2_2[i], end = '')
# print() # AzbycX
#
# r1 =  'abc'
#
# if r1 == r1[::-1]:
#     print('True')
# else:
#     print('False')