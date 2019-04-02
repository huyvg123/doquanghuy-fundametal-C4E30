    
itemlist = ['T-Shirt', 'Sweater']
crud = input("Welcome to our shop, what do you want (C, R, U, D)? ")
while True:
    if crud in ('r','R'):
        print('Our items:',end = ' ')
        for i in range(len(itemlist)):
            print(itemlist[i],end = ' ')
    elif crud == 'c':
        newitem = input('Enter new item:')
        itemlist.append(newitem)
        print('Our items:',end = ' ')
        for i in range(len(itemlist)):
            print(itemlist[i],end = ' ')
    elif crud == 'u':
        up = int(input('Update position:'))
        while True:
            if up > len(itemlist):
                up = int(input('No item in this position, please re-enter:'))
            else:
                break
        updateitem = input('New item:')
        itemlist[up-1] = updateitem
        print('Our items:',end = ' ')
        for i in range(len(itemlist)):
            print(itemlist[i],end = ' ')
    elif crud == 'd':
        dp = int(input('Delete position:'))
        while True:
            if dp > len(itemlist):
                dp = int(input('No item in this position, please re-enter:'))
            else:
                break
        del itemlist[dp-1]
        print('Our items:',end = ' ')
        for i in range(len(itemlist)):
            print(itemlist[i],end = ' ')
    else:
        print('Re-enter',end = '')
    print()
    crud = input('Choose your command (C, R, U, D):')