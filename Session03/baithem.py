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
