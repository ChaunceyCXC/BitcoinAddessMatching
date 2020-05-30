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
output ="/home/chauncey/avertical"


vendors=os.listdir(root)
for vendor in vendors:
    os.mkdir(output+"/"+vendor)
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
    newdic={}
    for key in addressdic:
        if addressdic[key]>1:
            newdic[key]=addressdic[key]

    writeToJSONFile(output+"/"+vendor+"/"+"frequency",newdic)
    print(max)
    print(n)
    addressdic.clear()

    for key in newdic:
        files = os.listdir(root+"/"+vendor)
        files.sort()
        for file in files:
            n=0
            fp = open(root+"/"+vendor + "/" + file, "r")
            for line in fp:
                add = json.loads(line)
                if add==key:
                    n=1
            writeToJSONFile(output +"/"+vendor+ "/" + key, n)



