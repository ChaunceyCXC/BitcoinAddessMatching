//Parse full Bitcoin transaction information to json file 

import os
import json
from blockchain_parser.blockchain import Blockchain


def writeToJSONFile(filePath, data):
    with open(filePath, 'a') as fp:
        json.dump(data, fp)
        fp.write("\n")


outputPath = "Path to save data"


blockchain = Blockchain(os.path.expanduser('path of Bitcoin raw data'))

for block in blockchain.get_unordered_blocks():
    filename = block.header.timestamp.strftime('%Y-%m-%d-%H:%M:%S') + ".json"
    #filename = block.header.timestamp.strftime('%Y-%m-%d') + ".json"
    filePath = rootPath + str(filename)

    for tx in block.transactions:
        data={}
        inputlist = []
        for no, input in enumerate(tx.inputs):
            sender = {'index': no, 'transaction_hash': input.transaction_hash,
                      'transaction_index': input.transaction_index}
            inputlist.append(sender)
        outputlist = []
        for no, output in enumerate(tx.outputs):
            if(output.value!=0):
                if(output.script.value!='INVALID_SCRIPT'):
                  if (len(output.addresses) == 1):
                     address = str(output.addresses[0])
                     receiver = {'index': no, 'address': address[13:-1], 'value': output.value}
                     outputlist.append(receiver)
        data[tx.hash] = {"timestamp": str(block.header.timestamp), "inputs": inputlist, 'outputs': outputlist}
        writeToJSONFile(filePath, data)
