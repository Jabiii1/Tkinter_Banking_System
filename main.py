from LogIn import logInWindow
from CreateAccount import accountWindow
from openpyxl import *

app = accountWindow()
app.runCreateAccount()

name = app.getName()
print(name)

wb = load_workbook("Userdata.xlsx")
ws= wb["User Database"]
ws.append = ([name, name , name])
wb.save("Userdata.xlsx")

print("Successfullu Done")
