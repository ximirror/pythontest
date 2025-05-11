@echo off

echo file to be imported: %1
python -m ExcelImport
echo =====================
echo please modify the file Parameter.py
echo =====================
pause

echo starting import export
python -m ExcelImport %1

pause