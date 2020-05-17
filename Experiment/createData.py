
import random
import os.path
import json
import datetime
import numpy as np

def writeToJSONFile(filePath, data):
    with open(filePath, 'a') as fp:
        json.dump(data, fp)
        fp.write("\n")


addressfolder="/home/chauncey/filteraddresstx"
output="/home/chauncey/CreateData"



files=os.listdir(addressfolder)

for file in files:
    fopen=open(addressfolder+"/"+file,"r")
    for line in fopen:
        tx=json.loads(line)
        n=random.randint(1,3)
        if(n==1):
            dict= {}
            key1 = list(tx.keys())[0]
            date1 = datetime.datetime.strptime(key1, '%Y-%m-%d-%H:%M:%S')
            value = tx[key1]
            hp1 = np.random.normal(0, 12)
            bitcoinvalue = (value / 0.94) / (1 + hp1 / 100)
            hp2=np.random.normal(0.5,0.6)
            datestring=(date1-datetime.timedelta(hours=hp2)).strftime('%Y-%m-%d-%H:%M:%S')
            dict["Date"]=datestring
            dict["bitcoin"]=bitcoinvalue
            writeToJSONFile(output + "/" + file, dict)