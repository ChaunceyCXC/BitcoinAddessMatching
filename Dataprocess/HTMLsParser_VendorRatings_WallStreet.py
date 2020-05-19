import glob
import re
import json
import csv
from bs4 import BeautifulSoup
import datetime
if __name__ == '__main__':
    # The output file name
    sOutputDirectory = "/home/chauncey/vendors/"
    sOutputJsonFilename = sOutputDirectory + "VendorRatings.json"
    sOutputCSVFilename = sOutputDirectory + "VendorRatings.csv"
    # This variable is used to store all comments
    aTableComments = []
    # Input directory
    sInputDirectory = "/home/chauncey/data_WallStreet/"
    sInputDirectoryQuery = sInputDirectory + "contactMember?member=*&tab=ratings#tabChooser"
    aListOfAllHTMLFiles = glob.glob(sInputDirectoryQuery)
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
                'rating': 0,
                'text': None,
                'buyer_ID': None,
                'money': 0,
                'vendor_ID': None
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
                break;

            daysnumber=int(list[0])
            enddate=datetime.date(2018,10,10)
            begindate=enddate-datetime.timedelta(days=daysnumber)
            aOneComment['date'] = str(begindate)[0:10]
            aRatingHTML = aAllCells[1]
            aListOfGoldStar = aRatingHTML.findChildren(alt="gold")
            aOneComment['rating'] = len(aListOfGoldStar)
            sCommentString = aAllCells[2].string
            aOneComment['text'] = sCommentString[7:len(sCommentString)-5]
            aOneComment['buyer_ID'] = aAllCells[3].string.replace(" ", "")
            aOneComment['money'] = float(aAllCells[4].string[3:])
            aOneComment['vendor_ID'] = sVendorID
            # Add this comment to the table of comments
            aTableComments.append(aOneComment)

    print("Total number of ratings: %d", len(aTableComments))

    # Write the table of comments into a json file.
    fp = open(sOutputJsonFilename, 'w')
    json.dump(aTableComments, fp)
    fp.close()

    # Write the table of comments into a csv file.
    fp = open(sOutputCSVFilename, 'w', encoding="utf-8", newline='')
    output = csv.writer(fp)  # create a csv.write
    output.writerow(aTableComments[0].keys())  # header row
    for row in aTableComments:
        output.writerow(row.values())  # values row
    fp.close()
