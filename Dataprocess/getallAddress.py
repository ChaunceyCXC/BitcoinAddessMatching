import os
import json


def writeToJSONFile(filePath, data):
    with open(filePath, 'a') as fp:
        json.dump(data, fp)
        fp.write("\n")


outputfile="/home/chauncey/Result/addressDic.json"
outputfile1="/home/chauncey/Result/addressDic1.json"
outputfile2="/home/chauncey/Result/addressFre.json"

addresslist=[]
rootPath = "/home/chauncey/DataWith32Eu/"
files=os.listdir(rootPath)
for file in files:
    fp=open(rootPath+file,"r")
    for line in fp:
       tx=json.loads(line)
       addresslist.append(tx["address"])
print(len(addresslist))
dict = {}
for key in addresslist:
    dict[key] = dict.get(key,0) + 1
print(len(dict))
newlist=[]
delelist=[]
for key in dict:
    n=dict[key]
    if n <20:
       delelist.append(key)
       continue
    newlist.append(key)

print(len(newlist))
ind=0
addressDict = {}
addressDict1 = {}
for i in newlist:
    addressDict[ind]= i
    addressDict1[i]=ind
    ind = ind + 1
writeToJSONFile(outputfile, addressDict)
writeToJSONFile(outputfile1, addressDict1)

for key in delelist:
    del dict[key]

writeToJSONFile(outputfile2, dict)
