
import json



def writeToJSONFile(filePath, data):
    with open(filePath, 'a') as fp:
        json.dump(data, fp)
        fp.write("\n")

if __name__ == '__main__':
    # The output file name
    sOutputDirectory = "/home/chauncey/WallStreetVendors/"
    rootPath="/home/chauncey/WallStreetData.json"
    fp = open(rootPath, "r")
    for line in fp:
        tx=json.loads(line)
        filename=tx["vendor_global_ID"]
        review={}
        review["Date"]=tx["date"]
        review["bitcoin"] = tx["bitcoin"]
        writeToJSONFile(sOutputDirectory+filename,review)

