import sys
from CSVDataExtractor import Column as ImportColumn, XLSXImporter as Importer
from ExcelExport import Column as ExportColumn, XLSXWriter, Averager
from Parameter import Parameter

class ExcelImport:
    
    def initializeImportColumns(self):
        for importData in self.parameter.importLocations:
            self.importColumns.append(ImportColumn(importData.startRow, importData.column))
            
    def initializeExportColumns(self):
        assert(len(self.importColumns) == len(self.parameter.outputLocations))
        for i in range(0, len(self.importColumns)):
            if self.parameter.outputLocations[i].makeAverage:
                self.exportColumns.append(Averager(
                    self.parameter.outputLocations[i].column,
                    self.parameter.outputLocations[i].startRow,
                    self.importColumns[i].data
                ))
            else:
                self.exportColumns.append(ExportColumn(
                    self.parameter.outputLocations[i].column,
                    self.parameter.outputLocations[i].startRow,
                    self.importColumns[i].data
                ))
    
    def __init__(self, _file):
        print("__init__(ExcelImport)")
        self.parameter = Parameter()
        self.file = _file
        self.importColumns = []
        self.exportColumns = []
        self.initializeImportColumns()
        
        self.success = False
        
    def run(self):
        
        try:
            importer: Importer = Importer(self.file)
            importer.open()
            importer.doImport(self.importColumns)
            self.initializeExportColumns()
            importer.close()
            
            exporter: XLSXWriter = XLSXWriter(self.parameter)
            exporter.open()
            exporter.doExport(self.exportColumns)
            exporter.write(self.parameter.outputPath)
            exporter.close()
            
            self.success = True
        except:
            print("something went wrong :/", file=sys.stderr)
            print(repr(sys.exc_info()), file=sys.stderr)
            self.success = False
        
                        
    def __enter__(self):        
        print("__enter__(ExcelImport)")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):        
        print("__exit__(ExcelImport)")
        
    def printParameter(self):
        self.parameter.print()
        
    def printResult(self):
        if self.success:
            print("hurray")
        else:
            print("oh no")
        
                
        
        
        
if __name__ == '__main__':
    # importer = ExcelImport(sys.argv[1])
    # importer.__enter__()
    # importer.print()
    #importer.__exit__()
    if len(sys.argv) < 2:
        with ExcelImport(None) as importer:
            importer.printParameter()
    
    else:
        assert(sys.argv[1] is not None)
        with ExcelImport(sys.argv[1]) as importer:
            importer.run()
            importer.printResult()
    