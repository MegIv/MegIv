print('=========break&continue========')
for i in range(10):
    if i == 5:
        print(i)
        continue

for i in range(10):
    if i == 5:
        print(i)
        break

# for i in range(10):
#     if i == 5:
#         continue
#         print(i)
#
# for i in range(10):
#     if i == 5:
#         break
#         print(i)

print('===========NestedLopp==========')
adj = ['buah','enak']
fruits = ['apel','pisang']
for x in adj:
    for y in fruits:
        print(x,y)

print('=========Try/exp=======')
x = 5
y = '5'

try:
    z = x + y
except:
    z = x+str(y)
print(z)
