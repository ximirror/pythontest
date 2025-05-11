import numbers
from idlelib.run import get_message_lines
from  CSVDataExtractor import XLSXImporter
from  CSVDataExtractor import Column

class ExcelImport:
    def __init__(self, filename: object) -> None:
        self.filename = filename
        self.data = []

    def getaverage(self) -> float:
        sum = 0
        for value in self.data:
                sum = sum + value
        len = self.data.__len__()
        average = sum / len
        return average

    def getmedian(self) -> float:
        len = self.data.__len__()
        datacopy= self.data[:]
        datacopy.sort()

        if len % 2 == 0:
            median = (datacopy[int(len/2)] +datacopy[int(len/2)-1])/2
        else:
            median = datacopy[int(len/2)]
        return median

    def getmax(self) -> float:
        max = self.data[0]
        for value in self.data:
            if value > max:
                max = value
        return max

    def getmin(self) -> float:
        min = self.data[0]
        for value in self.data:
            if value < min:
                min = value
        return min

    def parsedata(self,source):
        values = source.split(";")
        for value in values:
            self.data.append(float(value))

    def import_data(self, data):
        for value in data:
            self.data.append(value)

if __name__ == '__main__':
    excel = ExcelImport("data.xlsx")
    excel.parsedata("0;2.5;-3.6;1.5;4.5;1;1;1;1;10000")
    max= excel.getmax()
    min= excel.getmin()
    average= excel.getaverage ()
    median= excel.getmedian ()
    print (f"min= {min}")
    print (f"max= {max}")
    print (f"average= {average}")
    print (f"median= {median}")

    ## Homework:
    ##import the CSVDataExtractor in this file
    ##open the test1.xlsx
    ##use import_data function
    ##print the max, min, average and median of column B and C
    ##the output shall be the following:
    ##"Column B: max 56 min 2 median 28 average 29"
    ##"Column C: max 84 min 3 median 42 average 43.5"
    importer=XLSXImporter("/home/xi/Downloads/Test1.xlsx")
    print("importer is an object")
    print(f"importers file is {importer.file}")
    importer.open()
    column=Column(0,0)
    column.setcolumn("AA")
    print(f"column is {column.column}")



