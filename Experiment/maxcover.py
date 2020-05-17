import json
import os
import datetime


def writeToJSONFile(filePath, data):
    with open(filePath, 'a') as fp:
        json.dump(data, fp)
        fp.write("\n")


#root   = "/home/chauncey/address/252"
#output ="/home/chauncey/address/252bit3"

root   = "/home/chauncey/matchedaddressofvendor"



vendors=os.listdir(root)
sum=0
half=0
x=0
for vendor in vendors:
    x = x + 1
    files = os.listdir(root+"/"+vendor)
    addressdic={}
    n=0
    max=0
    for file in files:
        n=n+1
        label={}
        fp=open(root+"/"+vendor+"/"+file,"r")
        for line in fp:
            add = json.loads(line)
            if add in addressdic:
               if add not in label:
                addressdic[add]=addressdic[add]+1
                if addressdic[add]>max:
                       max=addressdic[add]
            else:
               addressdic[add]=1
            label[add]=1

    print(max/n)
    print(x)
    if max/n>0.5:
        half=half+1
    sum=sum+max/n
print(sum)
print(half)
print(x)