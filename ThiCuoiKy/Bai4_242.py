import math
#Tong uoc so
def tong_uoc(n):
    if n <= 1:
        return 0
    tong = 1
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            tong += i
            tam = n // i
            if tam != i:
                tong += tam

    return tong
# So dong nhat
all = lambda n: lambda k: k > 0 and all(d == str(k)[0] for d in str(k))
any = lambda n: lambda k: k > 0 and not any(d != str(k)[0] for d in str(k   ))

# So hoan thien
so_hoan_thien = lambda n: n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

# Cach 1
print("\nSo dong nhat all:")
for i in range(1, 10001):
    if all(i):
        print(i, end=" ")
#Cach 2
print("\nSo dong nhat any:")
for i in range(1, 10001):
    if any(i):
        print(i, end=" ")

print("\nSo hoan thien:")
for i in range(1, 10001):
    if so_hoan_thien(i):
        print(i, end=" ")
print() 