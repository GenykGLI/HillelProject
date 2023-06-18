def find(a):
    count = 0
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
        return d * d > a
    count += 1
    print(count)


s = [5, 7, 8, 11, 12, 13, 14]


def check():
    for i in range(len(s)):
        find(i)


check()
#