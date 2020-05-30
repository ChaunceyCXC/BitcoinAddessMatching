import os.path
import json



def writeToJSONFile(filePath, data):
    with open(filePath, 'a') as fp:
        json.dump(data, fp)
        fp.write("\n")



pathledger="/media/chauncey/Elements/bitcoinTx/2018"
output="/home/chauncey/DataWith32Eu"


files=os.listdir(pathledger)
for file in files:
    block = open(pathledger + "/" + file, 'r')
    date=file
    for line in block:
         tx=json.loads(line)
         for key in tx:
            receivers=tx[key]["outputs"]
            senders=tx[key]["inputs"]
            le1=len(receivers)
            le2=len(senders)
            addresslist = []
            if le1>10 and le2>10:
              for receiver in receivers:
                  addresslist.append(receiver["address"])
            if "32Eup1TPADYTAa46wq48c7qmg7AuFwigeM" in addresslist:
              outputvalue=0
              for receiver in receivers:

                bitcoinvalue=receiver["value"]/100000000
                dic={}
                dic["address"]=receiver["address"]
                dic["date"]=date
                dic["value"]=bitcoinvalue
                filepath = output + "/"+date
                writeToJSONFile(filepath,dic)

