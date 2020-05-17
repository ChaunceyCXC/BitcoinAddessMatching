import numpy as np
import os.path
import json
from sklearn.cluster import KMeans



def writeToJSONFile(filePath, data):
    with open(filePath, 'a') as fp:
        json.dump(data, fp)
        fp.write("\n")


input="/home/chauncey/filteraddresstx"
output="/home/chauncey/statistics"

files=os.listdir(input)
dateset=[]
for file in files:
    fopen=open(input+"/"+file,"r")
    arr=[]
    dict={}
    dict["file"]=file
    for line in fopen:
        tx=json.loads(line)
        key = list(tx.keys())[0]
        if "startDate" not in dict:
           dict["startDate"]=key
        dict["endDate"] = key
        value=tx[key]
        arr.append(value)

    mean=np.mean(arr)
    var=np.var(arr)
    dict["mean"]=mean
    dict["var"]=var
    dict["std"]=np.std(arr)
    dateset.append([mean,var])
    writeToJSONFile(output + "/" + "statistics.json", dict)
X=np.array(dateset)
kmeans=KMeans(n_clusters=20,random_state=0).fit(X)
labels=kmeans.labels_.tolist()
print(labels)
length=len(labels)
i=0
for file in files:
    dict2={}
    lab=labels[i]
    i+=1
    dict2[file]=lab
    writeToJSONFile(output + "/" + "labels.json", dict2)