import json
import os
import numpy as np
import datetime


root="/home/chauncey/address/252bit1"


files=os.listdir(root)
arraylist=[]
count=0
for file in files:
    if file!="frequency":
        fp=open(root+"/"+file,"r")
        arr=[]
        count=0
        for line in fp:
            count+=1
            number=int(json.loads(line))
            arr.append(number)
    array=np.array(arr)
    arraylist.append(array)
arraylist1=arraylist.copy()
arraylist2=arraylist.copy()

target=np.zeros(count,dtype=int)
a=10
k=a

print(datetime.datetime.now())
while k>0:
   k=k-1
   currentsum = np.sum(target)
   currenttarget = target
   i=0
   label=0
   for arr in arraylist:
       newarry=np.bitwise_or(target,arr)
       newsum=np.sum(newarry)
       if newsum>currentsum:
           currentsum=newsum
           currenttarget=newarry
           label=i
       i+=1
   target=currenttarget
   del arraylist[label]

print(np.sum(target))
print(datetime.datetime.now())


# target=np.zeros(count,dtype=int)
# k=a
#
# while k>0:
#    k=k-1
#    currentsum = 0
#    currentarray=None
#    i=0
#    label=0
#    for arr in arraylist1:
#        newarry=arr
#        newsum=np.sum(arr)
#        if newsum>currentsum:
#            currentsum=newsum
#            currentarray=newarry
#            label=i
#        i+=1
#    target=np.bitwise_or(target,currentarray)
#    del arraylist1[label]
#
# print(np.sum(target))
#
# target=np.zeros(count,dtype=int)
# k=a
#
# while k>0:
#    k=k-1
#    arry=arraylist2[-1]
#    target=np.bitwise_or(target,arry)
#    del arraylist2[-1]
#
# print(np.sum(target))
