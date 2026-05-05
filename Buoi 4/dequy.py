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

def fibonacci(n):
    # Điểm dừng (Base case): F0 = 1 và F1 = 1
    if n == 0 or n == 1:
        return 1
    # Công thức đệ quy: Fn = Fn-1 + Fn-2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Kiểm tra với các ví dụ trong ảnh
n1 = 7
print(f"Với n = {n1}, số Fibonacci thứ {n1} là: {fibonacci(n1)}") # Kết quả: 13

n2 = 8
print(f"Với n = {n2}, số Fibonacci thứ {n2} là: {fibonacci(n2)}") # Kết quả: 21