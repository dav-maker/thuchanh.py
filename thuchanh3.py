# Bài 6: Đếm số lượng từ 'word' trong chuỗi S
S = """Chiều chiều trước bến Văn Lâu
Ai ngồi, ai câu, ai sầu, ai thảm
Ai thương, ai cảm, ai nhớ, ai trông
Thuyền ai thấp thoáng ven sông
Đưa câu mái vẩy chạnh lòng nước non"""

word = input("Nhập từ cần đếm (word): ") # Nhập vào là: ai

# Bước 1: Loại bỏ dấu phẩy để từ không bị dính ký tự đặc biệt
S_bonus = S.replace(",", "")

# Bước 2: Tách chuỗi thành một danh sách các từ
danh_sach_tu = S_bonus.split()

# Bước 3: Đếm đúng từ 'word' (phân biệt hoa thường)
# Lúc này "Ai" (viết hoa) sẽ KHÔNG được đếm, chỉ đếm "ai" (viết thường)
so_luong = danh_sach_tu.count(word)

print(f"Số từ {word} là {so_luong}")

#Bai 12
import re

def chuan_hoa_chuoi(s):
    # 1. Xóa khoảng trắng đầu/cuối
    s = s.strip()
    
    # 2. Thay nhiều khoảng trắng thành 1
    s = re.sub(r'\s+', ' ', s)
    
    # 3. Xóa khoảng trắng trước dấu . ,
    s = re.sub(r'\s+([.,])', r'\1', s)
    
    # 4. Đảm bảo sau dấu . , có 1 khoảng trắng
    s = re.sub(r'([.,])([^\s])', r'\1 \2', s)
    
    return s


# Test
chuoi = "  Que huong " \
" Que  huong  la  chum  khe  ngot . " \
" Cho  con treo hai moi ngay  ,  " \
" Que  huong   la con   duong   di  hoc  . " \
"Con   ve   rop buom  vang   bay  ." \
" Do   Trung  Quan "
print(chuan_hoa_chuoi(chuoi))


#I
from datetime import datetime

# Lấy thời gian hiện tại từ hệ thống
now = datetime.now()

print(f"{'THÔNG TIN CẦN HIỂN THỊ':<40} | {'KẾT QUẢ'}")
print("-" * 60)

# 1. Năm hiện tại
print(f"{'Năm hiện tại':<40} | {now.year}")

# 2. Tháng hiện tại bằng chữ
print(f"{'Tháng hiện tại bằng chữ':<40} | {now.strftime('%B')}")

# 3. Tuần hiện tại là tuần thứ mấy trong năm
print(f"{'Tuần hiện tại là tuần thứ mấy trong năm':<40} | {now.strftime('%U')}")

# 4. Tuần hiện tại là tuần thứ mấy trong tháng
# Công thức: (ngày - 1) // 7 + 1
week_of_month = (now.day - 1) // 7 + 1
print(f"{'Tuần hiện tại là tuần thứ mấy trong tháng':<40} | {week_of_month}")

# 5. Ngày hiện tại là ngày thứ mấy trong năm
print(f"{'Ngày hiện tại là ngày thứ mấy trong năm':<40} | {now.strftime('%j')}")

# 6. Ngày dương lịch hiện tại là ngày
print(f"{'Ngày dương lịch hiện tại là ngày':<40} | {now.day}")

# 7. Thứ của ngày hiện tại
print(f"{'Thứ của ngày hiện tại':<40} | {now.strftime('%A')}")

# 8. Giờ phút giây hiện tại
print(f"{'Giờ phút giây hiện tại':<40} | {now.strftime('%H:%M:%S')}")

#II
from datetime import date

print("--- Nhập thông tin cho ngày thứ nhất ---")
d1 = int(input("Nhập ngày: "))
m1 = int(input("Nhập tháng: "))
y1 = int(input("Nhập năm: "))

print("\n--- Nhập thông tin cho ngày thứ hai ---")
d2 = int(input("Nhập ngày: "))
m2 = int(input("Nhập tháng: "))
y2 = int(input("Nhập năm: "))

# Tạo đối tượng date cho 2 mốc thời gian
ngay_1 = date(y1, m1, d1)
ngay_2 = date(y2, m2, d2)

# Tính toán sự chênh lệch
# Dùng hàm abs() để đảm bảo kết quả luôn dương dù bạn nhập ngày nào trước
khoang_cach = abs((ngay_2 - ngay_1).days)

print(f"\n=> Số ngày cách nhau giữa hai ngày là: {khoang_cach} ngày.")

#III
from datetime import datetime

# 1. Cho nhập chuỗi từ bàn phím (hoặc gán trực tiếp theo đề bài)
# Chuỗi mẫu: Sep 18 2019 2:43PM
chuoi_s = input("Nhập chuỗi ngày tháng (Ví dụ: Sep 18 2019 2:43PM): ")

# 2. Định nghĩa định dạng (format) của chuỗi đầu vào
# %b: Tháng viết tắt (Sep)
# %d: Ngày (18)
# %Y: Năm 4 chữ số (2019)
# %I:%M%p: Giờ (12h):Phút và AM/PM
dinh_dang = "%b %d %Y %I:%M%p"

try:
    # 3. Chuyển đổi chuỗi sang đối tượng datetime
    ngay_chuyen_doi = datetime.strptime(chuoi_s, dinh_dang)

    print("\n--- Kết quả sau khi chuyển đổi ---")
    print(f"Kiểu dữ liệu: {type(ngay_chuyen_doi)}")
    print(f"Giá trị ngày: {ngay_chuyen_doi}")
    
except ValueError:
    print("\nLỗi: Định dạng chuỗi bạn nhập không khớp với mẫu 'Sep 18 2019 2:43PM'")

#IV
from datetime import datetime, timedelta

# 1. Lấy thời gian hiện tại
now = datetime.now()
print(f"Thời gian hiện tại:  {now.strftime('%H:%M:%S')}")

# 2. Tạo một khoảng thời gian chênh lệch là 5 giây
khoang_cho = timedelta(seconds=5)

# 3. Cộng thêm vào thời gian hiện tại
thoi_gian_moi = now + khoang_cho

print(f"Thời gian sau 5 giây: {thoi_gian_moi.strftime('%H:%M:%S')}")