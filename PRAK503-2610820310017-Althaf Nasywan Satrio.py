import sys


def maksimal(a, b):
    if a > b:
        return a
    return b


def minimal(a, b):
    if a < b:
        return a
    return b


data = sys.stdin.read().split()
bilangan = int(data[0])
maks = -100000
minim = 100000
batas = 0
while batas < bilangan:
    nilai = int(data[1 + batas])
    maks = maksimal(maks, nilai)
    minim = minimal(minim, nilai)
    batas += 1
print(maks, minim)