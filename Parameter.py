import re

class Parameter:
            
    def __init__(self):
        self.importLocations = []
        self.outputLocations = []
        self.templatePath = None
        self.outputPath = None
        
        ############################################
        ### Customize this section !! ##############
        
        ### Start point of the columns for the data to be imported:
        self.importLocations.append(self.DataToImport(_A1Notation = "C2"))
        self.importLocations.append(self.DataToImport(_A1Notation = "E2"))
        self.importLocations.append(self.DataToImport(_A1Notation = "K2"))
        
        ### Start point of the columns in the template where the data is written
        self.outputLocations.append(self.DataExportLocation(_A1Notation = "A9"))
        self.outputLocations.append(self.DataExportLocation(_A1Notation = "B9"))
        self.outputLocations.append(self.DataExportLocation(_A1Notation = "D2", _makeAverage=True))
        
        ### path to the template (must be an xlsx!)
        self.templatePath = "./Copy of MTR data processing template .xlsx"
        ### name of sheet in the template
        self.templateSheet = "calcu"
        
        ### path to the final output file
        self.outputPath = "./output.xlsx"
        
        assert(len(self.importLocations) == len(self.outputLocations))
        assert(self.templatePath is not None)
        assert(self.templateSheet is not None)
        assert(self.outputPath is not None)
        
    def print(self):
        for i in range(0, len(self.importLocations)):
            print("import data from {} to {}, function: {}".format(self.importLocations[i].textRepresentation, self.outputLocations[i].textRepresentation, self.outputLocations[i].function))
            
        print("Template file: {}, sheet: {}".format(self.templatePath, self.templateSheet))
        print("writing to output file {}".format(self.outputPath))
            
    
    def convertA1Notation(_cellID: str) -> tuple:
        column: int = 0
        row: int = 0
        rowID = re.findall("[0-9]", _cellID, flags=re.IGNORECASE)
        columnID = re.findall("[A-Z]", _cellID, flags=re.IGNORECASE)
        exp: int = len(columnID) - 1
        for char in columnID:
            if char is None or len(char) == 0:
                continue
            column += (ord(char) - ord('A') + 1) * pow(26, exp)
            exp -= 1
            
        exp = len(rowID) - 1
        for digit in rowID:
            if digit is None or len(digit) == 0:
                continue
            row += (ord(digit) - ord('0')) * pow(10, exp)
            exp -= 1
            
        return [column - 1, row - 1]    # return index 0-based
            
    
    class DataToImport:
        """_summary_ This structure holds the location for a single column that needs to be extracted from the csv
        """
        
        def __init__(self, *, _A1Notation: str):
            """_summary_

            Args:
                _A1Notation (str): _column where the input data is read from, i.e. the first cell of the whole column_
            """
            cell = Parameter.convertA1Notation(_A1Notation)
            self.startRow = cell[1]
            self.column = cell[0]
            self.textRepresentation = _A1Notation
            
    class DataExportLocation:
        """_summary_ This structure defines the location where the data should be written to"""
        
        def __init__(self, *, _A1Notation: str, _makeAverage: bool = False):
            """_summary_

            Args:
                _A1Notation (str): _column where the data is put, i.e. the first cell in the column where data is written_
            """
            cell = Parameter.convertA1Notation(_A1Notation)
            self.startRow = cell[1]
            self.column = cell[0]
            self.makeAverage = _makeAverage
            self.textRepresentation = _A1Notation
            if _makeAverage:
                self.function: str = "Averaging"
            else:
                self.function: str = "importing"
        
if __name__ == "__main__":
    test = Parameter.convertA1Notation("A1")
    assert([0, 0] == test)
    test = Parameter.convertA1Notation("AA110")
    assert([26, 109] == test)
    p = Parameter()
    print("OK!")