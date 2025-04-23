from customtkinter import *

class accountWindow:
    def __init__(self):
        
        def updateDays(choice):
            self.birthDay.configure(values=self.days[choice])
            self.birthDay.set(self.days[choice][0])
        
        self.accWindow = CTk()
        self.accWindow.geometry("420x400")
        self.accWindow.title("Create an Account")
        self.accWindow.resizable(False, False)
        set_appearance_mode("light")

        #Months
        self.months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"]
        
        #Days
        self.days = {
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
        
        #Years
        self.years = [str(i) for i in range(1935, 2026)]
        
        self.title = CTkLabel(master=self.accWindow, text="Create your Account!",font=("Roboto", 24, "bold"), text_color="#031927")
        self.title.pack(pady=10)

        self.firstName = CTkEntry(master=self.accWindow, placeholder_text="First Name")
        self.firstName.pack(pady=5)

        self.middleName = CTkEntry(master=self.accWindow, placeholder_text="Middle Name")
        self.middleName.pack(pady=5)

        self.surName = CTkEntry(master=self.accWindow, placeholder_text="Surname")
        self.surName.pack(pady=5)

        self.Age = CTkEntry(master=self.accWindow, placeholder_text="Age")
        self.Age.pack(pady=5)

        self.sex = CTkComboBox(master=self.accWindow, values=["Male", "Female"], state="readonly")
        self.sex.pack(pady=5)

        self.birthMonth = CTkComboBox(master=self.accWindow, values=self.months, state="readonly")
        self.birthMonth.pack(pady=5)

        self.birthDay = CTkComboBox(master=self.accWindow, values=self.days["January"], state="readonly")
        self.birthDay.pack(pady=5)

        self.birthYear = CTkComboBox(master=self.accWindow, values=self.years, state="readonly")
        self.birthYear.pack(pady=5)

        self.birthMonth.configure(command=updateDays)

        self.createAccount = CTkButton(master=self.accWindow, text="Create Account", font=("Roboto", 14, "bold"), text_color="#FFFFFF")
        self.createAccount.pack(pady=5)
    
    def runCreateAccount(self):
        self.accWindow.mainloop()