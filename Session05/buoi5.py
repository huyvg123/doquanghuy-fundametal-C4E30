# def tong_binh_phuong(a,b): 
#     print(a+b)
#     return None
# tong = tong_binh_phuong(4,5)
# print(tong)


# def add_two_number(a,b): 
#     return a + b

# num1 = int(input('nhap so thu nhat: '))
# num2 = int(input('Nhap so thu hai: '))
# num3 = int(input('Nhap so thu ba: '))
# sum_3 = add_two_number(add_two_number(num1, num2),num3)
# print('Tong cac so la: ', sum_3)

# def add_two_number(): 
#     a = int(input('nhap so thu nhat: '))
#     b = int(input('Nhap so thu hai: '))
#     print('Tong cua hai so la: ', a+b)
# add_two_number()

# def say_hi(): 
#     print('hi')
#     print('bye')
# say_hi()



from turtle import * 
for i in range(4): 
    forward(200)
    left(90)
mainloop()


# def input_list(): 
#     ds=[]
#     m = int(input('Nhập số phần tử: '))
#     for v in range(m): 
#         so = int(input('Nhập số: '))
#         ds.append(so)
#     return ds
# ds1 = input_list()
# print(ds1)



# x = int(input("nhap m: "))
# tong = 0
# for i in range(x): 
#     y = int(input("nhap so: "))
#     tong = tong + y
# print("tong day vua nhap la: ",tong)
# a = int(input('nhap n: '))
# sum = 0
# trung_binh_cong = 0
# for v in range(a): 
#     b = int(input('Nhap so: '))
#     sum = sum + b
#     trung_binh_cong = sum/a
# print("trung binh cong day vua nhap là: ",trung_binh_cong)