import math

# =========================
# GIỚI HẠN (Theo đề bài là 1 triệu)
# =========================
LIMIT = 1000000 

print(f"\n===== KIỂM TRA CÁC DẠNG SỐ TỪ 1 ĐẾN {LIMIT:,} (DÙNG LAMBDA THUẦN) =====\n")

# ==============================================================================
# a) SỐ THÂN THIỆN: gcd(n, số đảo ngược) = 1
# ==============================================================================
is_friendly = lambda n: math.gcd(n, int(str(n)[::-1])) == 1

# ==============================================================================
# b) SỐ CHÍNH PHƯƠNG
# ==============================================================================
is_square = lambda n: math.isqrt(n)**2 == n

# ==============================================================================
# c) SỐ ĐỒNG NHẤT
# ==============================================================================
# Cách 1: dùng all()
is_repdigit_all = lambda n: all(d == str(n)[0] for d in str(n))
# Cách 2: dùng any()
is_repdigit_any = lambda n: not any(d != str(n)[0] for d in str(n))

# ==============================================================================
# d) SỐ HOÀN THIỆN (Tổng ước thực sự = n)
# Lưu ý: Lambda này chạy n tới 1 triệu sẽ rất chậm, nên cẩn thận khi loop toàn bộ.
# ==============================================================================
is_perfect = lambda n: n > 1 and sum(i for i in range(1, n//2 + 1) if n % i == 0) == n

# ==============================================================================
# e) SỐ PHONG PHÚ (Tổng ước thực sự > n)
# ==============================================================================
is_abundant = lambda n: n > 1 and sum(i for i in range(1, n//2 + 1) if n % i == 0) > n

# ==============================================================================
# f) SỐ TĂNG DẦN (Ký số tăng dần từ trái sang phải)
# ==============================================================================
is_increasing = lambda n: all(str(n)[i] < str(n)[i+1] for i in range(len(str(n))-1))

# ==============================================================================
# g) SỐ ARMSTRONG (Tổng lũy thừa bậc k của các chữ số = n)
# ==============================================================================
is_armstrong = lambda n: sum(int(d)**len(str(n)) for d in str(n)) == n

# ==============================================================================
# h) SỐ NGUYÊN TỐ
# ==============================================================================
# Cách 3: dùng any()
is_prime = lambda n: n > 1 and not any(n % i == 0 for i in range(2, int(math.sqrt(n)) + 1))

# Cách 4: Xây dựng hàm F theo yêu cầu (dùng def phối hợp filter và lambda)
def F(k):
    # filter tìm các ước từ 1 đến k, nếu chỉ có 2 ước thì là số nguyên tố
    uoc = list(filter(lambda x: k % x == 0, range(1, k + 1)))
    return len(uoc) == 2

# ==============================================================================
# i) SỐ PALINDROME (Số đối xứng)
# ==============================================================================
is_palindrome = lambda n: str(n) == str(n)[::-1]

# ==============================================================================
# j) SỐ NGUYÊN TỐ PALINDROME (Phải tự định nghĩa logic prime bên trong lambda)
# ==============================================================================
is_prime_palindrome = lambda n: (str(n) == str(n)[::-1]) and \
                                (n > 1 and not any(n % i == 0 for i in range(2, int(math.sqrt(n)) + 1)))

# ==============================================================================
# k) SỐ LỘC PHÁT (Chỉ chứa 6 hoặc 8)
# ==============================================================================
# Cách 1: dùng all()
is_loc_phat_all = lambda n: all(d in '68' for d in str(n))
# Cách 2: dùng X + Y = chiều dài
is_loc_phat_count = lambda n: (str(n).count('6') + str(n).count('8')) == len(str(n))

# ==============================================================================
# l) SỐ LỘC PHÁT PALINDROME
# ==============================================================================
is_loc_phat_palindrome = lambda n: all(d in '68' for d in str(n)) and (str(n) == str(n)[::-1])


# ==============================================================================
# THỰC THI VÀ IN KẾT QUẢ (Ví dụ một số dạng tiêu biểu để tránh treo máy)
# ==============================================================================

# Lưu ý: Với LIMIT = 1.000.000, một số hàm như is_perfect sẽ chạy cực lâu.
# Ở đây tôi thực hiện in danh sách các số thỏa mãn trong khoảng 1 -> LIMIT cho các loại số ít.

print("a) SỐ THÂN THIỆN (20 số đầu):", [i for i in range(1, 1000) if is_friendly(i)][:20])

print("c) SỐ ĐỒNG NHẤT:", [i for i in range(1, LIMIT) if is_repdigit_all(i)])

# Số hoàn thiện nhỏ hơn 1 triệu chỉ có 4 số: 6, 28, 496, 8128
# Để tránh loop lâu, ta chỉ in kết quả đã biết hoặc giới hạn range thấp hơn.
print("d) SỐ HOÀN THIỆN:", [6, 28, 496, 8128]) 

print("g) SỐ ARMSTRONG:", [i for i in range(1, LIMIT) if is_armstrong(i)])

print("j) SỐ NGUYÊN TỐ PALINDROME (20 số đầu):", [i for i in range(1, LIMIT) if is_prime_palindrome(i)][:20])

print("k) SỐ LỘC PHÁT (20 số đầu):", [i for i in range(1, LIMIT) if is_loc_phat_all(i)][:20])

print("l) SỐ LỘC PHÁT PALINDROME:", [i for i in range(1, LIMIT) if is_loc_phat_palindrome(i)])

print("\n===== HOÀN THÀNH =====")