import glob
import re
import json
from bs4 import BeautifulSoup
import datetime


def writeToJSONFile(filePath, data):
    with open(filePath, 'a') as fp:
        json.dump(data, fp)
        fp.write("\n")

if __name__ == '__main__':
    # The output file name
    sOutputDirectory = "/home/chauncey/vendors/"
    sOutputJsonFilename = sOutputDirectory + "VendorRatings.json"

    # This variable is used to store all comments
    aTableComments = []
    # Input directory
    sInputDirectory = "/home/chauncey/Data/"
    sInputDirectoryQuery = sInputDirectory + "contactMember?member=*&tab=ratings#tabChooser"
    aListOfAllHTMLFiles = glob.glob(sInputDirectoryQuery)
    i=0
    for url in aListOfAllHTMLFiles:
        # Example: url = sOutputDirectory + "contactMember_member=2Trappy_tab=ratings#tabChooser.html"
        sVendorID = re.search('contactMember?member=(.+?)&tab=ratings#tabChooser', url)
        aOneVendorsRatingPage = open(url, encoding='utf-8')
        aBeautifulSoup = BeautifulSoup(aOneVendorsRatingPage, features="html.parser")
        aOneVendorsRatingPage.close()
        # search for the table
        aRatingTablesTemp = aBeautifulSoup.findChildren('table', {'class': 'ratingTable hoverable'})
        aRatingTable = aRatingTablesTemp[0]
        aAllRows = aRatingTable.findChildren('tr')
        nNumOfAddedComments = 0
        for aOneRow in aAllRows:
            # Create a new instance for a comment / row
            aOneComment = {
                'date': None,
                'money': 0,

            }
            # read all cells from a row of a table
            aAllCells = aOneRow.findChildren('td')
            nNumOfCells = len(aAllCells)
            if nNumOfCells < 5:
                print('skip one rating since the total number of cells is less than 5')
                continue
            datestring=aAllCells[0].string
            list=datestring.split('d')
            if   not list[0].isdigit():
                break

            daysnumber=int(list[0])
            enddate=datetime.date(2018,10,11)
            begindate=enddate-datetime.timedelta(days=daysnumber)
            aOneComment['date'] = str(begindate)[0:10]
            aOneComment['money'] = float(aAllCells[4].string[3:])


            # Add this comment to the table of comments
            aTableComments.append(aOneComment)
        if len(aTableComments)<200:
            continue
        if len(aTableComments)>5000:
            continue
        sOutputJsonFilename =sOutputDirectory+str(i)+".json"
        for dic in aTableComments:
            writeToJSONFile(sOutputJsonFilename,dic)
        i+=1

    print("Total number of ratings: %d", len(aTableComments))

