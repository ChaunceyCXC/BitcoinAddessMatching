import json
import os
import numpy as np
import datetime


#root="/home/chauncey/address/252"
dictfile="/home/chauncey/Result/addressDic.json"
folder="/home/chauncey/avertical"


addressDic={}
f=open(dictfile)
for line in f:
    addressDic=json.loads(line)
x=0
n=0
y=0
vendors=os.listdir(folder)
for vendor in vendors:
    root=folder+"/"+vendor
    addressls=[]
    vendorlist=vendor.split("-")
    for vendoritem in vendorlist:
        addressls.append(addressDic[vendoritem])
    files=os.listdir(root)
    arraylist=[]
    addresslist=[]
    count=0
    for file in files:
        if file!="frequency":
            addresslist.append(file)
            fp=open(root+"/"+file,"r")
            arr=[]
            count=0
            for line in fp:
                count+=1
                number=int(json.loads(line))
                arr.append(number)
            array=np.array(arr)
            arraylist.append(array)
    if count>=200 and count <1200:
        n += 4
        target=np.zeros(count,dtype=int)

        a=0.51
        k=100
        selectaddress=[]
        oldupdate=1
        while k>0:
           if len(addresslist)==0:
               break
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
           newupdate=currentsum-np.sum(target)
           ratio=float(newupdate) / float(oldupdate)
           if ratio<a:
               break;
           oldupdate=newupdate
           target=currenttarget
           selectaddress.append(addresslist[label])
           del addresslist[label]
           del arraylist[label]
        l=len(selectaddress)
        y+=l
        for add in selectaddress:
            for tadd in addressls:
                if add==tadd:
                    x+=1
print(x)
print(n-x)
print(y-x)
print(float(2*x)/float(2*x+n-x+y-x))
