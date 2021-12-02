array = [1,2,3,4,5]
n = len(array)
n = n-1
pos = input('Choose position from 0 to %d   ' % n)
try:
    pos = int(pos)
    array1 = array[0:pos]
    array2 = array[pos:n]
    for i in array1:
        array2.append(i)
    print(array2)
except:
    print('invalid position')