
import json

root="/home/chauncey/address/295bit1/frequency"


fp=open(root,"r")
fre={}
for line in fp:
    fre=json.loads(line)

number1=0
number2=0
other=0
total=0
for key in fre:
    number=fre[key]
    if int(number)==1:
        number1+=1
    elif int(number)==2:
        number2+=1
    else:
        other+=1
    total+=1

print(number1,number2,other,total)