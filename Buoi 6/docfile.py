import zlib
import os

def giai_bai_tap_tong_hop():
    file_goc = 'test.txt'
    file_nen = 'test_nen.dat'

    # --- BƯỚC 0: TỰ TẠO FILE TXT BÊN TRONG CODE ---
    noi_dung_tho = """Thuyền và biển
Chỉ có thuyền mới hiểu
Biển mênh mông nhường nào
Chỉ có biển mới biết
Thuyền đi đâu về đâu"""

    # Ghi nội dung vào file test.txt (tạo file mới nếu chưa có)
    with open(file_goc, 'w', encoding='utf-8') as f:
        f.write(noi_dung_tho)
    print(f"-> Đã tự động tạo file: {file_goc}")


    # --- YÊU CẦU 1: Đọc file gốc và xuất ra file mới giảm dung lượng ---
    with open(file_goc, 'r', encoding='utf-8') as f:
        data = f.read()
    
    # Nén dữ liệu (chuyển sang byte rồi nén)
    data_bytes = data.encode('utf-8')
    compressed_data = zlib.compress(data_bytes)
    
    # Ghi ra file nén (dạng nhị phân 'wb')
    with open(file_nen, 'wb') as f:
        f.write(compressed_data)
    
    size_goc = os.path.getsize(file_goc)
    size_nen = os.path.getsize(file_nen)
    
    print(f"1. Đã tạo file giảm dung lượng: {file_nen}")
    print(f"   Dung lượng gốc: {size_goc} bytes")
    print(f"   Dung lượng sau nén: {size_nen} bytes")


    # --- YÊU CẦU 2: Đọc file đã nén và trả về định dạng ban đầu ---
    print("\n2. Đang đọc file nén và phục hồi định dạng...")
    with open(file_nen, 'rb') as f:
        compressed_content = f.read()
    
    # Giải nén và chuyển lại thành văn bản (decode)
    original_content = zlib.decompress(compressed_content).decode('utf-8')
    
    print("-" * 30)
    print(original_content) # In ra màn hình để kiểm tra
    print("-" * 30)

# Chạy toàn bộ chương trình
if __name__ == "__main__":
    giai_bai_tap_tong_hop()