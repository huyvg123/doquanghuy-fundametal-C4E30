print('Bài 1: ')
inventory = {
    'good' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedrool', 'bread loaf']
}
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
a = inventory['backpack']
del a[1]
for i in range(0,1,len(inventory)): 
    inventory['good']  += 50 
print(inventory)
print()
print('Bài 2: ')
prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
}
stock = {
    "banana" : 6,
    "apple" : 0, 
    "orange" : 1.5,
    "pear" : 3
}
sum1 = {}
for v in prices: 
    print(v)
    print("prices = ",prices)
    print("stock = ", stock)
    sum1[v] = prices[v] + stock[v]
print(sum1)
sum2 = 0
for i in range(len(sum1)): 
    sum2 = sum2 + sum1[v]
print
print("sum = ", sum2)
print('Bài 3: ')
ket_qua_sai = ('1. ', '2. ', '3. ')
ket_qua_dung = ('4. ')
while True:
    print("Answer the following algebra question:")
    print('If x = 8, then what is the value of 4(x + 3) ?')
    print('1. 35')
    print('2. 36')
    print('3. 40')
    print('4. 44')
    dap_an = input("Your choise: ")  
    if dap_an in ket_qua_dung: 
        print("bingo")
        break
    else: 
        print(":(")
print()
print('Bài 4: ')
dap_an_sai = ('1.','2. ','3. ')
dap_an_dung = ('4. ') 
print("Answer the following algebra question:")
print('If x = 8, then what is the value of 4(x + 3) ?')
print('1. 35')
print('2. 36')
print('3. 40')
print('4. 44')
dap_an1 = input("Your choise: ")  
if dap_an1 in dap_an_dung: 
    print("bingo")
    x = 1
else: 
    print(":(")
    x = 0 
dung = ('2. ')
sai = ('1. ','3. ','4. ') 
print('Estimate this answer(exact calculation not needed):')
print('Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?')
print('1. About 55')
print('2. Abuot 65')
print('3. Abuot 75')
print('4. Abuot 85')
dap_an_2 = input("your choise: ")
if dap_an_2 in dung: 
    print("bingo")
    y = 1
else: 
    print(':(')
    y = 0
print('You correctly answer',x+y,'out of 2 question')