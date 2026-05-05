n = int(input('Nhap so nguyen duong n: '))

so_chan = 0
so_le = 0

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        so_chan += 1
    else:
        so_le += 1
    n //= 10

    print('so luong so chan = ',so_chan)
    print('so luong so le = ',so_le)

--2
n = int(input("Nhập số nguyên dương n: "))
temp_n = n
tong = 0
tich = 1

while temp_n > 0:
    chu_so = temp_n % 10
    tong += chu_so
    tich *= chu_so
    temp_n //= 10

print(f"Tổng={tong}, Tích={tich}")


--3
n_str = input("Nhập số nguyên n: ")
la_so_may_man = True

for char in n_str:
    if char != '6' and char != '8':
        la_so_may_man = False
        break

if la_so_may_man:
    print(f"{n_str} là số may mắn.")
else:
    print(f"{n_str} KHÔNG phải số may mắn.")

--4
n = int(input("Nhập số nguyên dương n: "))
max_digit = 0
temp_n = n

while temp_n > 0:
    chu_so = temp_n % 10
    if chu_so > max_digit:
        max_digit = chu_so
    temp_n //= 10

print(f"Số lớn nhất={max_digit}")