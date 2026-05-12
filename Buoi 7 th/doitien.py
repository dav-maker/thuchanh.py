def doi_tien():
    # Danh sách 9 loại mệnh giá tiền theo thứ tự giảm dần
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    
    try:
        # Nhập số tiền X từ người dùng
        X = int(input("Nhập số tiền X: "))
        so_tien_ban_dau = X
        
        print(f"\nSo tien {so_tien_ban_dau} duoc doi thanh:")
        
        tong_so_to = 0
        
        # Duyệt qua từng mệnh giá để tính số tờ
        for loai in menh_gia:
            so_to = X // loai  # Chia lấy phần nguyên để tìm số tờ
            X = X % loai       # Lấy phần dư còn lại sau khi đổi
            
            print(f"Loai {loai:>3} gom {so_to} to")
            tong_so_to += so_to
            
        print("-" * 20)
        print(f"TỔNG CỘNG CÓ {tong_so_to} TỜ")
        
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên dương.")

if __name__ == "__main__":
    doi_tien()