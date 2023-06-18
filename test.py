s = [2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 15, 16, 17, 45, 55, 59]
lst = []


def find(a):
    poz = 0
    for i in range(1, a + 1):
        if a % i == 0:
            poz += 1
    if poz == 2:
        lst.append(a)


def check():
    for i in s:
        find(i)
    print(f'Count of prime numbers is ', len(lst))


check()
