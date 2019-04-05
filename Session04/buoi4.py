dic = {"computer":"maytinh", "mouse":"chuot","keyboard":"banphim"}

while True: 
    tu = input("mời nhập từ: ")
    if tu == "exit": 
        break
    if tu in dic: 
        print("Nghĩa của từ là: ", dic[tu])
    else: 
        print("Từ này không có trong từ điển " )


