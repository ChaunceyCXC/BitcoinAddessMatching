import json






root="/home/chauncey/Result/addressDic.json"

with open(root) as jsonfile:
    addressDic=json.load(jsonfile)


address=addressDic["2368"]
print(address)