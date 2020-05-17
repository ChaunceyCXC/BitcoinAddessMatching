import json
import os
import datetime
import time

root   = "/home/chauncey/fullledger1"
output ="/home/chauncey/address1/timesearching"

review="/home/chauncey/Reviews/1000"

def writeToJSONFile(filePath, data):
    with open(filePath, 'a') as fp:
        json.dump(data, fp)
        fp.write("\n")
#os.mkdir(output)
#vendors=os.listdir(review)
time1=datetime.datetime.now()
print(datetime.datetime.now())
#for vendor in vendors:
fp = open(review, "r")
for line in fp:
    fb = json.loads(line)
    date=fb["Date"]
    value=fb["bitcoin"]*0.945
    x = date[11:13]
    date1 = datetime.datetime.strptime(date, '%Y-%m-%d-%H:%M:%S')
    if x != 12:
        files = os.listdir(root)
        for file in files:
            filename=file[:-5]
            date2 = datetime.datetime.strptime(filename, '%Y-%m-%d-%H:%M:%S')
            ddiff = date2 - date1
            days, seconds = ddiff.days, ddiff.seconds
            hours = days * 24 + seconds / 3600
            if hours > 0 and hours < 1 or hours > 12 and hours < 13:
                fp = open(root +"/"+ file, "r")
                for line in fp:
                    tx = json.loads(line)
                    vdiff = abs(( tx["value"]-value)) /value  # Comapring Money
                    if (vdiff < 0.1):

                        add=tx["address"]
                        #writeToJSONFile(output+"/"+date, add)
    else:
        files = os.listdir(root)
        for file in files:
            filename=file[:-5]
            date2 = datetime.datetime.strptime(filename, '%Y-%m-%d-%H:%M:%S')
            ddiff = date2 - date1
            days, seconds = ddiff.days, ddiff.seconds
            hours = days * 24 + seconds / 3600
            if hours > 0 and hours < 1 or hours > -12 and hours < -11:
                fp = open(root +"/"+ file, "r")
                for line in fp:
                    tx = json.loads(line)
                    vdiff = abs(( tx["value"]-value)) /value  # Comapring Money
                    if (vdiff < 0.1):

                        add=tx["address"]
                       # writeToJSONFile(output+"/"+date, add)

time2=datetime.datetime.now()
print(time2)
df=time2-time1
print(df.seconds)