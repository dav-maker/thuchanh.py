
cd = input('Nhap chieu dai day hinh chu nhat: ')
cr = input('Nhap chieu rong day hinh chu nhat: ')
cc = input('Nhap chieu cao day hinh chu nhat: ')
sole = input('So luong so le can hien thi: ')
format_str = '{:.'+sole+'f}'

cd = float(format_str.format(eval(cd)))
cr = float(format_str.format(eval(cr)))
cc = float(format_str.format(eval(cc)))


dien_tich = cd * cr 
dien_tich = float(format_str.format(dien_tich))
the_tich = cd * cr * cc
the_tich = float(format_str.format(the_tich))

print('Dien tich day hinh chu nhat = ',dien_tich, 'cm²')
print('The tich hinh khoi = ',the_tich, 'cm³')