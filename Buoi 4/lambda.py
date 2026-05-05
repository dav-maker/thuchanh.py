# 6. Anonymous Function (lambda)

import math

# a) Giá trị tuyệt đối của n
ttd = lambda n: abs(n)

# b) Giá trị của n + 15
plus_15 = lambda n: n + 15

# c) Tích của x và y
Tich = lambda x, y: x * y

# d) Kiểm tra n có là bội số của 13 hoặc 19 hay không
is_multiple_13_19 = lambda n: n % 13 == 0 or n % 19 == 0

# e) Diện tích hình tròn
DTht = lambda r: math.pi * r * r

# f) Chu vi hình chữ nhật
cvhcn = lambda d, r: 2 * (d + r)

# g) Kiểm tra số chính phương
scp = lambda n: int(math.sqrt(n)) ** 2 == n

# h) Kiểm tra số nguyên tố
snt = lambda n: (
    False if n < 2 else
    all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))
)

# i) Kiểm tra tam giác và loại tam giác
triangle_type = lambda a, b, c: (
    "Không phải tam giác"
    if a + b <= c or a + c <= b or b + c <= a
    else "Tam giác đều"
    if a == b == c
    else "Tam giác vuông cân"
    if (a == b or b == c or a == c) and
       (a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a)
    else "Tam giác vuông"
    if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a
    else "Tam giác cân"
    if a == b or b == c or a == c
    else "Tam giác thường"
)

# ==========================
# Nhập dữ liệu và kiểm tra
# ==========================

n = int(input("Nhập số nguyên n: "))
print("a) |n| =", ttd(n))
print("b) n + 15 =", plus_15(n))
print("d) Là bội của 13 hoặc 19:", is_multiple_13_19(n))
print("g) Là số chính phương:", scp(n))
print("h) Là số nguyên tố:", snt(n))

x = int(input("\nNhập x: "))
y = int(input("Nhập y: "))
print("c) x * y =", Tich(x, y))

r = float(input("\nNhập bán kính hình tròn r: "))
print("e) Diện tích hình tròn =", DTht(r))

d = float(input("\nNhập chiều dài hình chữ nhật: "))
rong = float(input("Nhập chiều rộng hình chữ nhật: "))
print("f) Chu vi hình chữ nhật =", cvhcn(d, rong))

a = int(input("\nNhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))
print("i) Loại tam giác:", triangle_type(a, b, c))