from LogIn import logInWindow
from CreateAccount import accountWindow
from openpyxl import *

app = accountWindow()
app.runCreateAccount()

name = app.getName()
print(name)

#Test ng Database
wb = load_workbook("Userdata.xlsx")
sheet = wb.active
sheet["A2"] = name
wb.save("Userdata.xlsx")

print("Successfully Done")
