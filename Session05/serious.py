print('7. ')
def remove_dollar_sign(s) : 
    return s.replace('$','')
s = input('Nhap s :')
print(remove_dollar_sign(s))
print()
print('8. ')
def remove_dollar_sign(s) : 
    return s.replace('$','')
s = input('Nhap s :')
print(remove_dollar_sign(s))
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")
print()
print('9. ')   
def get_even_list(l) :
    get_even = []
    for i in l :
        if i % 2 ==0 :
            get_even.append(i)
    return get_even
x = int(input('Số phần tử: '))
l = []
for i in range(x) :
    y = int(input('Nhap :'))
    l.append(y)
print(get_even_list(l))
print()
print('10. ')
def get_even_list(l) :
    get_even = []
    for i in l :
        if i % 2 ==0 :
            get_even.append(i)
    return get_even
x = int(input('Số phần tử: '))
even_list = get_even_list([1, 2, 5, 9, -10, 6])
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
print()
print('11. and 12. ')
def is_inside(point,rectangle):
    if (rectangle[0] <= point[0] <= rectangle[0]+rectangle[2]) and (rectangle[1] <= point[1] <= rectangle[1]+rectangle[3]):
        return True
    else:
        return False
check = is_inside([200, 120], [140, 60, 100, 200])
if check == True:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")

    