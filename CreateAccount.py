from customtkinter import *

accWindow = CTk()
accWindow.geometry("420x400")
accWindow.title("Create an Account")
accWindow.resizable(False, False)
set_appearance_mode("light")

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"]
    
days = {
    "January": [str(i) for i in range(1, 32)],
    "February": [str(i) for i in range(1, 30)],
    "March": [str(i) for i in range(1, 32)],
    "April": [str(i) for i in range(1, 32)],
    "May": [str(i) for i in range(1, 32)],
    "June": [str(i) for i in range(1, 31)],
    "July": [str(i) for i in range(1, 32)],
    "August": [str(i) for i in range(1, 32)],
    "September": [str(i) for i in range(1, 31)],
    "October": [str(i) for i in range(1, 32)],
    "November": [str(i) for i in range(1, 31)],
    "December": [str(i) for i in range(1, 32)],
}

def update_days(choice):
    birthDay.configure(values=days[choice])
    birthDay.set(days[choice][0])

title = CTkLabel(master=accWindow, text="Create your Account!",font=("Roboto", 24, "bold"), text_color="#031927")
title.pack(pady=10)

firstName = CTkEntry(master=accWindow, placeholder_text="First Name")
firstName.pack(pady=5)

middleName = CTkEntry(master=accWindow, placeholder_text="Middle Name")
middleName.pack(pady=5)

surName = CTkEntry(master=accWindow, placeholder_text="Surname")
surName.pack(pady=5)

Age = CTkEntry(master=accWindow, placeholder_text="Age")
Age.pack(pady=5)

birthMonth = CTkComboBox(master=accWindow, values=months, state="readonly")
birthMonth.pack(pady=5)

birthDay = CTkComboBox(master=accWindow, values=days["January"], state="readonly")
birthDay.pack(pady=5)


birthMonth.configure(command=update_days)
aeuiuyuuoghjfgjfnjfth
accWindow.mainloop()