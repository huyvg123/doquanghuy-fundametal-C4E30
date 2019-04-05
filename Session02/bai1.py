n = int(input('Moi ban nhap phan tu: '))
ds = []
for v in range(n): 
    so = int(input('nhap phan tu: '))
    ds.append(so)
print('day so vua nhap la: ')
for v in ds: 
    print(v, end = ' ')
sum = 0 
tong_so_chan = 0 
for v in ds: 
    if v % 2 == 0: 
        sum += v 
        tong_so_chan += 1 
print('trung binh cac so chan la:  ', sum/tong_so_chan)



# sotien = input('Nhập số tiền gửi: ')
# while True: 
#     sotien = sotien + sotien * 6.5/100
#     for i in range(9): 
        
#         if len(sotien) >= 9: 
#             break
#         else: 
#             print('sai')



# password = input('Nhập pass: ')
# while True: 
#     if len(password) >= 8: 
#         break
#     else: 
#         print('Mã không hợp lệ.')
#         break
# print("Mã pass của bạn là: ", password)


# # for i in range(10): 
# #     print(i)
# #     break
# # # dem = 0 
# # # while True: 
# # #     print('hi', dem)
    
# # #     dem += 1
# # #     if dem >= 3: 
# # #         break