import math

# =========================
# Hàm kiểm tra số nguyên tố
# =========================
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


# ====================================
# Hàm đổi số sang dạng strobogrammatic
# ====================================
def strobogrammatic_number(n):

    # Quy tắc quay 180 độ
    rotate = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6'
    }

    s = str(n)
    result = ""

    # Đảo ngược rồi đổi số
    for ch in reversed(s):

        if ch not in rotate:
            return -1

        result += rotate[ch]

    return int(result)


# ====================================
# Kiểm tra số strobogrammatic
# ====================================
def is_strobogrammatic(n):
    return strobogrammatic_number(n) == n


# ====================================
# Kiểm tra strobogrammatic mở rộng
# (cho phép 2 và 5)
# ====================================
def is_extended_strobogrammatic(n):

    rotate = {
        '0': '0',
        '1': '1',
        '2': '2',
        '5': '5',
        '6': '9',
        '8': '8',
        '9': '6'
    }

    s = str(n)
    result = ""

    for ch in reversed(s):

        if ch not in rotate:
            return False

        result += rotate[ch]

    return int(result) == n


# ====================================
# a. In các số strobogrammatic < 1 triệu
# ====================================
print("a. So strobogrammatic < 1,000,000:")

for i in range(1000000):
    if is_strobogrammatic(i):
        print(i, end=" ")

print("\n")


# ====================================
# b. Số nguyên tố strobogrammatic
# ====================================
print("b. So nguyen to strobogrammatic:")

for i in range(1000000):
    if is_strobogrammatic(i) and is_prime(i):
        print(i, end=" ")

print("\n")


# ====================================
# c. Strobogrammatic mở rộng
# ====================================
print("c. So strobogrammatic mo rong:")

for i in range(1000000):
    if is_extended_strobogrammatic(i):
        print(i, end=" ")

print("\n")


# ====================================
# d. Số nguyên tố strobogrammatic mở rộng
# ====================================
print("d. So nguyen to strobogrammatic mo rong:")

for i in range(1000000):
    if is_extended_strobogrammatic(i) and is_prime(i):
        print(i, end=" ")

print("\n")


# ====================================
# e. Không phải strobogrammatic,
# không phải số nguyên tố,
# nhưng strobogrammatic của nó là số nguyên tố
# ====================================
print("e. Dieu kien dac biet:")

for i in range(1000000):

    strobo = strobogrammatic_number(i)

    if strobo == -1:
        continue

    if (not is_strobogrammatic(i)
            and not is_prime(i)
            and is_prime(strobo)):

        print(i, "->", strobo)