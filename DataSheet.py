from openpyxl import load_workbook, workbook
from openpyxl.chart import title
import shutil
import os

shutil.copy("EmptyDataSheet.xlsx", "Data/Cliente2.xlsx")

Data = load_workbook("Data/Cliente2.xlsx")
Ficha = Data.active

Ficha["B3"] = "Holasss"
Ficha["B2"] = "Que talwdwd"

Data.save(filename = "Data/Cliente2.xlsx")

os.startfile("Data\Cliente2.xlsx", "print")