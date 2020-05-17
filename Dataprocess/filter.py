
import random
import os.path
import json
import datetime
import numpy as np

def writeToJSONFile(filePath, data):
    with open(filePath, 'a') as fp:
        json.dump(data, fp)
        fp.write("\n")


addressfolder="/home/chauncey/vendors"
output="/home/chauncey/filtervendors"
ratefolder="/home/chauncey/rate.json"

ratedict={}
dicopen =open(ratefolder,"r")
for line in dicopen:
    ratedict=json.loads(line)
dicopen.close()
'''
files=os.listdir(addressfolder)

for file in files:
    filepath=addressfolder+"/"+file
    fopen=open(filepath,"r")
    n=0
    for line in fopen:
        n+=1

    if n>1000:
        os.remove(filepath)
'''

files=os.listdir(addressfolder)

for file in files:
    n=0
    fopen=open(addressfolder+"/"+file,"r")
    for line in fopen:
        tx=json.loads(line)
        key1 = list(tx.keys())[0]
        key2=list(tx.keys())[1]
        datestring=tx[key1]
        usvalue=tx[key2]
        date1 = datetime.datetime.strptime(datestring, '%Y-%m-%d')
        if date1<datetime.datetime(2018,4,11):
            continue
        changerate=ratedict[datestring]
        value = float(usvalue)/changerate
        dict={}
        dict[datestring]=value
        writeToJSONFile(output + "/" + file, dict)

