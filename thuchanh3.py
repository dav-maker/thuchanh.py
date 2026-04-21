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