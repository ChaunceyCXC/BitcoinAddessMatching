import json
import os
import datetime


def writeToJSONFile(filePath, data):
    with open(filePath, 'a') as fp:
        json.dump(data, fp)
        fp.write("\n")


root   = "/home/chauncey/address/252"
output ="/home/chauncey/address/252bit3"

os.mkdir(output)
files = os.listdir(root)
addressdic={}
for file in files:
    label={}
    fp=open(root+"/"+file,"r")
    for line in fp:
        add = json.loads(line)
        if add in addressdic:
           if add not in label:
            addressdic[add]=addressdic[add]+1
        else:
           addressdic[add]=1
        label[add]=1
newdic={}
for key in addressdic:
    if addressdic[key]>2:
        newdic[key]=addressdic[key]

writeToJSONFile(output+"/"+"frequency",newdic)

addressdic.clear()

for key in newdic:
    files = os.listdir(root)
    files.sort()
    for file in files:
        n=0
        fp = open(root + "/" + file, "r")
        for line in fp:
            add = json.loads(line)
            if add==key:
                n=1
        writeToJSONFile(output + "/" + key, n)



