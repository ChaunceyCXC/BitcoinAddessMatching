
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
output="/home/chauncey/Experiment1/K1"


files=os.listdir(addressfolder)

for file in files:
    fopen=open(addressfolder+"/"+file,"r")
    for line in fopen:
        tx=json.loads(line)
        key1 = list(tx.keys())[0]
        date1 = datetime.datetime.strptime(key1, '%Y-%m-%d-%H:%M:%S')


        date2=date1

        value=tx[key1]
        hp1=np.random.normal(5,2)
        bitcoinvalue=value*(1+hp1/100)
        n=random.randint(1,2)
        if(n==1):
            dict= {}
            datestring=date2.strftime('%Y-%m-%d-%H:%M:%S')
            dict["Date"]=datestring
            dict["bitcoin"]=bitcoinvalue
            writeToJSONFile(output + "/" + file, dict)
            dict2 = {}
            date2string = (date2+datetime.timedelta(days=1)).strftime('%Y-%m-%d-%H:%M:%S')
            dict2["Date"] = date2string
            dict2["bitcoin"] = bitcoinvalue
            writeToJSONFile(output + "/" + file, dict2)
            dict3 = {}
            date3string = (date2+datetime.timedelta(days=2)).strftime('%Y-%m-%d-%H:%M:%S')
            dict3["Date"] = date3string
            dict3["bitcoin"] = bitcoinvalue
            writeToJSONFile(output + "/" + file, dict)