import random

a = 1

b = 99

hads = random.randint(a, b)

print(hads)

javab = input("doroste ? :")

while javab != 'd' or javab != 'y':
    if javab == 'k':
        b = hads
        hads = random.randint(a, b-1)
        print(hads)
        javab = input("doroste ? :")
    if javab == 'b':
        a = hads
        hads = random.randint(a+1, b)
        print(hads)
        javab = input("doroste ? :")

print('Wowwww!, I did it!')