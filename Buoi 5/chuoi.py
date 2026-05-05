from collections import Counter

# Nhập chuỗi
s1 = input("Nhập S1: ")
s2 = input("Nhập S2: ")

# Đưa về dict (Counter)
dict1 = Counter(s1)
dict2 = Counter(s2)

# a) Ký tự xuất hiện trong cả 2
common = dict1 & dict2
print("Ký tự xuất hiện trong cả 2:", list(common.elements()))

# b) Đếm ký tự có trong S1 nhưng không có trong S2 và ngược lại
count_s1_not_s2 = 0
for ch in dict1:
    if ch not in dict2:
        count_s1_not_s2 += 1

count_s2_not_s1 = 0
for ch in dict2:
    if ch not in dict1:
        count_s2_not_s1 += 1

print("Số ký tự có trong S1 nhưng không có trong S2:", count_s1_not_s2)
print("Số ký tự có trong S2 nhưng không có trong S1:", count_s2_not_s1)

# c) Dò S1 trên dict2 và dò S2 trên dict1
only_s1 = []
for ch in dict1:
    if ch not in dict2:
        only_s1.append(ch)

only_s2 = []
for ch in dict2:
    if ch not in dict1:
        only_s2.append(ch)

print("Ký tự có trong S1 nhưng không có trong S2:", only_s1)
print("Ký tự có trong S2 nhưng không có trong S1:", only_s2)