import math

# Ham snt
def LaSNT(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def cau_1():

    try:
        x = input("Nhap so cach nhau boi (,):  ")
        a, b = map(int, x.split(','))
        
        start = min(a, b)
        end = max(a, b)
        
        for i in range(start, end + 1):
            print(f"Bang cuu chuong {i}:")
            for j in range(1, 11):
                print(f"{i} x {j} = {i * j}")
            print("-" * 15)
    except ValueError:
        print("Nhap lai a va b")


def cau_2():
    n = int(input("Nhap so nguyen duong n: "))
    if LaSNT(n):
        print(f"{n} la so nguyen to.")
    else:
        print(f"{n} Khong phai la so nguyen to.")

# --- BÀI 3 ---
def cau_3():
    n = int(input("Nhap so nguyen duong n: "))
    uoc_so = [i for i in range(1, n) if LaSNT(i)]
    print(f"{uoc_so}")

print(cau_1())
print(cau_2())
print(cau_3())