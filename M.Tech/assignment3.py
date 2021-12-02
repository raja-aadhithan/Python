list=[29,24,25,26,27]
print ("original list:",list)

list.extend([50,60])
print ("list after adding 58 and 60: ", list)

list.remove(24) 
list.remove(27)
print ("list after removing 24 and 27: ", list)

list.sort()
print ("ascending order:", list)

list.reverse() 
print ("descending order:", list)

print ("length of list:", len(list))

s =0
for i in range (0,len(list)): s = s+list[i] 
print ("sum of all elements",s)

s =0
for i in range (0,len(list)): 
    if(list[i]%2 ==0) :s = s+list[i] 
print ("sum of all even elements",s)

s =0
for i in range (0,len(list)): 
    if(list[i]%2 ==1) :s = s+list[i] 
print ("sum of all odd elements",s)

c =0
s =0
list2 =[]
for i in range (0,len(list)):
    for a in range (2,list[i]):
        if (list[i]%a == 0): c = c+1
    if (c==0):list2.append(list[i])
    c =0
for b in range (0, len(list2)): s = s+list2[b] 
print ("sum of all prime elements",s)

index= list.index(25) 
print ("index of 25 is:",index)

del list[:]
print ("List after deleting",list)