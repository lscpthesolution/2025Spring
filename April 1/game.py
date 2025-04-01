import gspread
import random 
from oauth2client.service_account import ServiceAccountCredentials

class VocabFromGSheet:

    def __init__(self, jsonFile):
        # Define scope for Google Sheets and Drive
        self.scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        # Load credentials from JSON key file
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(jsonFile, self.scope)
        # Authorize and connect to Google Sheets
        self.client = gspread.authorize(self.creds)
    
    def openGSheet(self, sheetName):    
        # Open the spreadsheet by name
        self.sheet = self.client.open(sheetName).sheet1

    def getAllValues(self):
        # Get all values
        return self.sheet.get_all_values()
    
    def makeDictionaries(self):
        target = self.getAllValues()
        words = list(each[0] for each in target)
        meanings = list(each[1] for each in target)
        examples = list(each[2] for each in target)

        self.wordToDefinitions = dict(zip(words, meanings))
        self.wordToExamples = dict()
        for each in range(len(words)):
            if(words[each] in self.wordToExamples):
                self.wordToExamples[words[each]].append(examples[each])
            else:
                self.wordToExamples.update({words[each]:[examples[each]]})

    def getWordToExamples(self):
        return self.wordToExamples
    
    def getWordToDefinition(self):
        return self.wordToDefinitions

    def display(self, mode="word"):
        if(mode == "definition"):
            for each in self.wordToDefinitions:
                print(each, " : ", self.wordToDefinitions[each])
        elif(mode == "example"):
            for each in self.wordToExamples:
                if(len(self.wordToExamples[each]) > 1):
                    for other in self.wordToExamples[each]:
                        print(each, " : ", other)
                else:
                    print(each, " : ", self.wordToExamples[each][0])
        else:
            for each in self.wordToDefinitions:
                print(each)



class Game:

    def __init__(self):
        self.myJson = "YOUR JASON FILE"
        self.myGSheet = "YOUR VOCAB GOOGLE SPREADSHEET FILE"

    def ready(self):
        self.vocab = VocabFromGSheet(self.myJson)
        self.vocab.openGSheet(self.myGSheet)
        self.vocab.makeDictionaries()
