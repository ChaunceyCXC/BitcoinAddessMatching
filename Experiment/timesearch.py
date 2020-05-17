import json
import os
import datetime
from datetime import timedelta

class Node(object):
    def __init__(self):
        self.father = None
        self.left = None
        self.right = None
        self.split = None
root   = "/home/chauncey/fullledger"
output ="/home/chauncey/address1/kdtimesearching2"

rootnode=Node()

review="/home/chauncey/Reviews/1000"
def writeToJSONFile(filePath, data):
    with open(filePath, 'a') as fp:
        json.dump(data, fp)
        fp.write("\n")

def constructsplittree( splitlist):
    node=Node()
    node.split=splitlist[0]
    size=int((len(splitlist)-1)/2)
    if  size==0:
         return node
    leftlist=splitlist[1:size+1]
    rightlist=splitlist[size+1:]
    node.left=constructsplittree(leftlist)
    node.right=constructsplittree(rightlist)
    return node
def findAllpathDate(onode,valueh,valuel,dateh,datel,path):

    split1=datetime.datetime.strptime(onode.split, '%Y-%m-%d-%H:%M:%S')
    newpath1 = path + "/" + "Left"
    newpath2 = path + "/" + "Right"
    if dateh<=split1:
        pathes=[]
        if onode.left==None:
            pathes.append(newpath1)
            return pathes
        pathes=findAllpathValue(onode.left,valueh,valuel,dateh,datel,newpath1)
        return pathes
    elif date1>split1:
        pathes = []
        if onode.left == None:
            pathes.append(newpath2)
            return pathes
        pathes=findAllpathValue(onode.right,valueh, valuel, dateh, datel, newpath2)
        return pathes
    else:
        pathes1 = []
        pathes2 = []
        if onode.left == None:
            pathes1.append(newpath1)
            pathes2.append(newpath2)
            return pathes1 + pathes2
        pathes1=findAllpathValue(onode.left,valueh,valuel,dateh,datel,newpath1)
        pathes2=findAllpathValue(onode.right,valueh,valuel,dateh,datel,newpath2)
        return pathes1+pathes2


def findAllpathValue(onode, valueh, valuel, dateh, datel, path):
    split1 = float(onode.split)
    newpath1 = path + "/" + "Left"
    newpath2 = path + "/" + "Right"
    if valueh <= split1:
        pathes = []
        if onode.left == None:
            pathes.append(newpath1)
            return pathes
        pathes = findAllpathDate(onode.left, valueh, valuel, dateh, datel, newpath1)
        return pathes
    elif valuel > split1:
        pathes = []
        if onode.left == None:
            pathes.append(newpath2)
            return pathes
        pathes = findAllpathDate(onode.right, valueh, valuel, dateh, datel, newpath2)
        return pathes
    else:
        pathes1 = []
        pathes2 = []
        if onode.left == None:
            pathes1.append(newpath1)
            pathes2.append(newpath2)
            return pathes1 + pathes2
        pathes1 = findAllpathDate(onode.left, valueh, valuel, dateh, datel, newpath1)
        pathes2 = findAllpathDate(onode.right, valueh, valuel, dateh, datel, newpath2)
        return pathes1 + pathes2
#os.mkdir(output)
#vendors=os.listdir(review)

f=open("/home/chauncey/fullledger/0split.json","r")
ls=[]
for line in f:
    s=json.loads(line)
    ls.append(s["split"])
node=constructsplittree(ls)
print(datetime.datetime.now())
#for vendor in vendors:
fp = open(review, "r")
for line in fp:
    fb = json.loads(line)
    date=fb["Date"]
    value=fb["bitcoin"]*0.945
    x = date[11:13]
    date1 = datetime.datetime.strptime(date, '%Y-%m-%d-%H:%M:%S')
    valueh=value*1.1
    valuel=value*0.9
    dateh=date1+timedelta(hours=1)
    datel=date1
    pathset=findAllpathDate(node,valueh, valuel, dateh, datel, root)
    for path in pathset:
        files = os.listdir(path)
        for file in files:
            filename=file[:-5]
            date2 = datetime.datetime.strptime(filename, '%Y-%m-%d-%H:%M:%S')
            ddiff = date2 - date1
            days, seconds = ddiff.days, ddiff.seconds
            hours = days * 24 + seconds / 3600
            if hours > 0 and hours < 1 or hours > 12 and hours < 13:
                fp = open(path +"/"+ file, "r")
                for line in fp:
                    tx = json.loads(line)
                    vdiff = abs(( tx["value"]-value)) /value  # Comapring Money
                    if (vdiff < 0.1):
                        add=tx["address"]
                        #writeToJSONFile(output+"/"+date, add)

print(datetime.datetime.now())