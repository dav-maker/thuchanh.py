from collections import Counter

# Nhập chuỗi
s1 = input("Nhập chuỗi S1: ")
s2 = input("Nhập chuỗi S2: ")

# Đưa về Counter
c1 = Counter(s1)
c2 = Counter(s2)

# a) Ký tự xuất hiện trong cả 2 chuỗi
common = c1 & c2
print("Ký tự xuất hiện trong cả 2:", list(common.elements()))

# b) Đếm ký tự chỉ có ở mỗi chuỗi
only_s1 = set(s1) - set(s2)
only_s2 = set(s2) - set(s1)

print("Số ký tự có trong S1 nhưng không có trong S2:", len(only_s1))
print("Số ký tự có trong S2 nhưng không có trong S1:", len(only_s2))

# c) In các ký tự riêng của mỗi chuỗi
print("Ký tự có trong S1 nhưng không có trong S2:", only_s1)
print("Ký tự có trong S2 nhưng không có trong S1:", only_s2)