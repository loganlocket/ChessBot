#For the import statments you will have to use 'pip3 install --user gspread oauth2client'
#And if that doesn't work just try 'pip3 install gspread oauth2client'

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('DataBaseTesting_JSON.json', scope)
client = gspread.authorize(creds)

sheet = client.open('DataBase1').sheet1

pp = pprint.PrettyPrinter()
#wholeThing = sheet.get_all_records()

class Spreadsheet:
    def __init__(self):
        self.mySheet = sheet

    def getSheet(self):
        return self.mySheet

    def appendRow(self, row, listToAdd):
        self.mySheet = self.mySheet.append_row(row, listToAdd)

    def appendCol(self, col, listToAdd):
        self.mySheet = self.mySheet.append_col(col, listToAdd)

mySheet = sheet.cell(2,2).value
pp.pprint(mySheet)
mySheet = sheet.update_cell(2, 2, 'pp')
mySheet = sheet.cell(2,2).value
pp.pprint(mySheet)
