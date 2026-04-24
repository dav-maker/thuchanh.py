def tong_chu_so(n):
    if n == 0:
        return 0
    return n % 10 + tong_chu_so(n // 10)

# Test
n = int(input("Nhập n: "))
print("Tổng chữ số =", tong_chu_so(abs(n)))

def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)

# Test
n = int(input("Nhập n: "))
print(f"{n}! =", giai_thua(n))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Test
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("UCLN =", gcd(a, b))