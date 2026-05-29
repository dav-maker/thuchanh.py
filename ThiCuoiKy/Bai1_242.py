#  Nhap du lieu
dai = float(input("Nhap chieu dai (cm): "))
rong = float(input("Nhap chieu rong (cm): "))
cao = float(input("Nhap chieu cao (cm): "))

# Nhap so le
so_le = int(input("So le can hien thi "))

# cong thuc 
dien_tich_day = dai * rong
the_tich = dien_tich_day * cao

# Ma Unicode
ma1 = "\u00b2"
ma2 = "\u00b3"
#Dien tich day
print(f"Dien tich day hinh chu nhat = {dien_tich_day:.{so_le}f}cm{ma1}")
#The tich
print(f"The tich hinh khoi = {the_tich:.{so_le}f}cm{ma2}")