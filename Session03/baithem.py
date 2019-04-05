#Bài 1: 
print("Bài 1: ")
#Tính số tiền sau 9 năm gửi
print("Câu a: ", end = " ")
x = int(input("Số tiền đã gửi là: "))
y = int(input("Số năm là: "))
i = 0
while i < y : 
    x = x + x*0.065
    i = i + 1 
print('Số tiền lúc sau là: ',x)
#Muốn mua nhà 1,2 tỉ thì số năm cần làm là? 
print("Câu b: ", end = " ")
a = int(input("Số tiền đã gửi là: "))
b = int(input("Số tiền cần rút là: "))
i = 0
while a < b: 
    a = a + a*0.065
    i = i + 1
print("Số tháng cần để rút là: ", i) 
# Gianha = 1200000000
# Tiengui = 21000000
# nam = 1
# while (nam <= 9):
#     Tiengui = Tiengui + Tiengui*6.5/100
#     nam += 1
# print('So tien thu duoc sau 9 nam', Tiengui)
# Tiengui = 21000000
# while (Tiengui <= Gianha):
#     Tiengui = Tiengui + Tiengui*6.5/100
#     nam += 1
# print('Sau ', nam,'nam a se mua duoc nha')