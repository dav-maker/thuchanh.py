import math
#kiem tra boi so
Boi_so = lambda n: n % 13 == 0 or n % 19 == 0

#kiem tra tam giac
Tam_giac = lambda a, b, c: ( "khong phai tam giac"
    if a + b <= c or a + c <= b or b + c <= a
    else "Tam giac deu"
    if a == b == c
    else "Tam giac vuong can"
    if (a == b or b == c or a == c) and
       (a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a)
    else "Tam giac vuong"
    if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a
    else "Tam giac can"
    if a == b or b == c or a == c
    else "Tam giac thuong"
)
#Nhap so nguyen
n = int(input("Nhap so nguyen n: "))
#Kiem tra boi so 13 hoac 19
print("Boi cua 13 hoac 19:", Boi_so(n))
#In ra loai tam giac
a = int(input("\nNhap canh a: "))
b = int(input("Nhap canh b: "))
c = int(input("Nhap canh c: "))
print("Loai tam giac:", Tam_giac(a, b, c))