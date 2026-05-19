# =========================================
# Sinh số Strobogrammatic gồm n chữ số
# =========================================

def generate_strobogrammatic(n, total_length):

    # Điều kiện dừng
    if n == 0:
        return [""]

    if n == 1:
        return ["0", "1", "8"]

    smaller = generate_strobogrammatic(n - 2, total_length)

    result = []

    for middle in smaller:

        # Không cho số bắt đầu bằng 0
        if n != total_length:
            result.append("0" + middle + "0")

        result.append("1" + middle + "1")
        result.append("6" + middle + "9")
        result.append("8" + middle + "8")
        result.append("9" + middle + "6")

    return result


# =========================================
# Sinh số Strobogrammatic mở rộng
# =========================================

def generate_extended_strobogrammatic(n, total_length):

    if n == 0:
        return [""]

    if n == 1:
        return ["0", "1", "2", "5", "8"]

    smaller = generate_extended_strobogrammatic(n - 2, total_length)

    result = []

    for middle in smaller:

        if n != total_length:
            result.append("0" + middle + "0")

        result.append("1" + middle + "1")
        result.append("2" + middle + "2")
        result.append("5" + middle + "5")
        result.append("6" + middle + "9")
        result.append("8" + middle + "8")
        result.append("9" + middle + "6")

    return result


# =========================================
# Chương trình chính
# =========================================

n = int(input("Nhap n (2 <= n <= 10): "))

while n < 2 or n > 10:
    n = int(input("Nhap lai n (2 <= n <= 10): "))


# =========================================
# a. Các số strobogrammatic
# =========================================

print("\na. So strobogrammatic gom", n, "chu so:")

strobo_numbers = generate_strobogrammatic(n, n)

for num in strobo_numbers:
    print(num)


# =========================================
# b. Các số strobogrammatic mở rộng
# =========================================

print("\nb. So strobogrammatic mo rong gom", n, "chu so:")

extended_numbers = generate_extended_strobogrammatic(n, n)

for num in extended_numbers:
    print(num)