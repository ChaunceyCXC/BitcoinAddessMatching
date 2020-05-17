import json
import os
import datetime

root = "/home/chauncey/DataWithEs"

files=os.listdir(root)
total=0;
for file in files:
     count=0
     fp=open(root+"/"+file,"r")
     for line in fp:
          count += 1
     total=total+count

print(total)
