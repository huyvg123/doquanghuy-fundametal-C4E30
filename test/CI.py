print('Bài 1: ')
print('Nhập vào 1 dãy số: ')
list = [1, 4, 1, 64, 128, 5, 4, 7, 32]
print(list)
list.reverse()
print('Dãy số vừa nhập theo chiều ngược: ')
for i in range(len(list)): 
    print(list[i])

print()
print('Bài 2: ')
list1= [1, 2, 4, 16, 64, 128, 256 ]
print('Trong dãy số: ', list1)
for i in range(0,len(list1)): 
    for n in range(i,len(list1)): 
        if list1[i] * list1[n] == 256: 
            print('Cặp số phân biệt sau có tích là 256:', list1[i],'-vị trí:',i,' và ', list1[n],'-vị trí:',n)