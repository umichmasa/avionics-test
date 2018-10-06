import csv

class Warning(object):
    def __init__(self, titles, tlm, mode, warnlow, warnhigh, helptxt, note):
        self.titles = titles
        self.tlm = tlm
        self.mode = mode
        self.warnlow = warnlow
        self.warnhigh = warnhigh
        self.helptxt = helptxt
        self.note = note

    def toString(self):
        string = 189*"-" + "\n"
        longestString = findLongestStr(readAndStoreSpreadsheet())
        for title in self.titles:
            if(len(title)<len(longestString)):
                title = makeStrSameLength(longestString, title)
            string += title + "\t" + "    |     "

        string += "\n" + 189*"-" + "\n"

        varList = [self.tlm,self.mode,self.warnlow,self.warnhigh,self.helptxt,self.note]
        for var in varList:
            currStr = str(var[0])
            if (len(currStr) < len(longestString)):
                currStr = makeStrSameLength(longestString, currStr)
            string += currStr + "\t" + "    |     "

        string += "\n"
        for var in varList:
            currStr = str(var[1])
            if (len(currStr) < len(longestString)):
                currStr = makeStrSameLength(longestString, currStr)
            string += currStr + "\t" + "    |     "

        string += "\n"
        for var in varList:
            currStr = str(var[2])
            if (len(currStr) < len(longestString)):
                currStr = makeStrSameLength(longestString, currStr)
            string += currStr + "\t" + "    |     "

        string += "\n"
        for var in varList:
            currStr = str(var[3])
            if (len(currStr) < len(longestString)):
                currStr = makeStrSameLength(longestString, currStr)
            string += currStr + "\t" + "    |     "

        string += "\n"

        return string

    def getTitles(self):
        return self.titles

    def getTlm(self):
        return self.tlm

    def getMode(self):
        return self.mode

    def getWarnLow(self):
        return self.warnlow

    def getWarnHigh(self):
        return self.warnhigh

    def getHelpTxt(self):
        return self.helptxt

    def getNote(self):
        return self.note





def readAndStoreSpreadsheet():
    data = [];
    with open('warnings.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            data.append(row)
            line_count += 1

    return data


def sortData(list, type, col, lowerbound):
    #The end goal here is to be able to return an array with the desired data type
    #We just want to be able to take the data from the warnings spreadsheet by column
    data = []
    currRow = 0;
    for row in list:
        if(currRow >= lowerbound):
            point = row[col]
            if(type == "string"):
                data.append(point)
            if(type == "float"):
                data.append(float(point))
        currRow+=1
    return data

def makeStrSameLength(targetStr,currStr):
    retval = currStr
    while(len(targetStr) > len(retval)):
        retval += " "
    return retval

def findLongestStr(list2d):
    retval = ""
    for row in list2d:
        for e in row:
            if(len(e)>len(retval)):
                retval = e
    return retval


def createWarningList():
    data = readAndStoreSpreadsheet()
    titles = data[0]
    tlm = sortData(data, "string", 0, 1)
    mode = sortData(data, "string", 1, 1)
    warnlow = sortData(data, "float", 2, 1)
    warnhigh = sortData(data, "float", 3, 1)
    helptxt = sortData(data, "string", 4, 1)
    note = sortData(data, "string", 5, 1)
    warning = Warning(titles,tlm,mode,warnlow,warnhigh,helptxt,note)
    print(warning.toString())
    return warning;

createWarningList()
print(createWarningList().getNote())