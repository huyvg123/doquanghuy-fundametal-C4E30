print('2.1: ', end = " ")
print("Hello, my name is Huy and there are my ship size: ")
size = [5, 7, 300, 90, 24, 50, 75]
print(size)
print()
print('2.2: ', end = ' ')
print('Now my biggest sheep has size', max(size), "let's shear it")
print()
print('2.3: ', end = ' ')
print("Now my bigget sheep has size 300 les't shear it")
for i in range(len(size)): 
    if(size[i] == max(size)): 
        v = i
        break
size[v] = 8        
print(size)
print()
print('2.4: ', end = ' ')
print('One minth has passed, now here is my flock')
for i in range(len(size)): 
    size[i] += 50 
print(size)
print()
print('2.5: ', end = ' ')
print('Hellon my name is Huy and here is my flock')
size = [5,7,300,90,24,50,75]
print(size)
for x in range(0,4):
    print('MONTH ', x, " :")
    print('One month has passed, now here is my flock')
    print(size)
    print('Now my biggest sheep has size', max(size), "Let's shear it")
    print('After shearing, here í my flock: ')
    for i in range(len(size)):
        if(size[i] == max(size)): 
            v = i
            break
    size[v] = 8
    print('One month has passed, now here is my flock: ')
    for i in range(len(size)): 
        size[i] += 50 
    print(size) 
print()
print('2.6: ',end = ' ')   
sum = 0
print('My flock has size in total: ', end =' ')
for i in range(len(size)):
    sum += size[i]
print(sum)
print('I would get: ', sum ,' *2$ =', sum*2,'$')



