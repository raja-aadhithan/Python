#This program finds the number of times a number has to be flipped and added to become a palindrome; the result also shows a graph.

import random
import matplotlib.pyplot as plt
arr_no =[]
arr_pl =[]
arr_ct =[]

def swap(x):
    s = 0
    c = -1
    w =0
    y =1
    m =x
    while(w-y != 0):
        #print (x)
        y = x
        for i in range(0,len(str(y))):
            sum = (x%10)*(10**(len(str(y))-1-i))
            s = s+ sum
            x = int(x/10)
        #print (s)
        w = s
        x = y+s
        s = 0
        c = c+1
        if (c>20) : 
            c=-1
            break
            
    #print ('original value',m,'resultant palindome',w,'count', c)
    arr_no.append(m)
    arr_pl.append(w)
    arr_ct.append(c)

for l in range(100,1000):
    swap(l)

plt.plot(arr_no, arr_ct, label = "line 1")
plt.show()
