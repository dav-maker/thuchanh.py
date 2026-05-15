import math

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Nhập danh sách
numbers = []

while True:
    n = int(input("Nhập số nguyên: "))
    numbers.append(n)

    choice = input("Bạn có muốn nhập tiếp không? (Y/N): ").strip().lower()
    if choice != 'y':
        break

# a) In số nguyên tố
primes = [x for x in numbers if is_prime(x)]
print("Các số nguyên tố:", primes)

# b) Tính trung bình cộng
negatives = [x for x in numbers if x < 0]
positives = [x for x in numbers if x > 0]

if negatives:
    avg_neg = sum(negatives) / len(negatives)
    print("Trung bình số âm:", avg_neg)
else:
    print("Không có số âm")

if positives:
    avg_pos = sum(positives) / len(positives)
    print("Trung bình số dương:", avg_pos)
else:
    print("Không có số dương")

# c) Số lớn nhất, nhỏ nhất
print("Số lớn nhất:", max(numbers))
print("Số nhỏ nhất:", min(numbers))

# d) Kiểm tra tăng dần
is_increasing = all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))

if is_increasing:
    print("Danh sách đã được sắp xếp tăng dần")
else:
    print("Danh sách chưa được sắp xếp tăng dần")