from decimal import Decimal


def zad1(str1="79-900", str2="80-155"):
    f = [int(str1[0:2]), int(str1[3:7])]
    s = [int(str2[0:2]), int(str2[3:7])]
    codes = []
    while s[1] + 1 != f[1]:
        codes.append(str(f[0]) + "-" + "%03d" % f[1])
        f[1] = 0 if f[1] == 999 else f[1] + 1
        f[0] = f[0] + 1 if f[1] == 0 else f[0]
    return codes


def zad2(arr=[2, 3, 7, 4, 9], n=10):
    return [x for x in list(range(1, n + 1)) if x not in arr]


def zad3(start=2, end=5.5):
    return [Decimal(str(x)) for x in [x * 0.5 for x in range(start * 2, int(end * 2 + 1))]]

