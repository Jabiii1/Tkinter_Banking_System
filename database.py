from openpyxl import Workbook
from customtkinter import *

workBook = Workbook()
workBookSave = workBook.active
workBookSave.title = "User Database"

workBookSave.append(["Name", "Age", "Gender"])

workBook.save("Userdata.xlsx")