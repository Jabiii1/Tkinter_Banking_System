from customtkinter import *

class logInWindow:
    def __init__(self):
        self.mainWindow = CTk()
        self.mainWindow.geometry("350x250")
        self.mainWindow.title("CashG Bank System")
        self.mainWindow.resizable(False, False)
        set_appearance_mode("Light")
        set_default_color_theme("dark-blue")
        
        #LabelLogin
        self.labelLogin = CTkLabel(master=self.mainWindow, text="Log In your CashG Account", font=("Roboto", 24, "bold"), text_color="#031927")
        self.labelLogin.pack(pady=10)
        
        #Entry for username
        self.entryUser = CTkEntry(master=self.mainWindow, width=200, height=24, placeholder_text="Username")
        self.entryUser.pack(pady=5)
        
        #Entry for password
        self.entryPass = CTkEntry(master=self.mainWindow, width=200, height=24, placeholder_text="Password", show="*")
        self.entryPass.pack(pady=10)
        
        #Button for login
        self.buttonLogIn = CTkButton(master=self.mainWindow, text="Log In", font=("Arial", 18, "normal"), text_color="#C8E0F4", fg_color="#031927", hover_color="#189000",width=200)
        self.buttonLogIn.pack(pady=5)
        
        #Frame for remember me and forget
        self.frame1 = CTkFrame(self.mainWindow)
        self.frame1.pack(padx=70,fill="both", expand=True)
        
        #Checkbutton for remember me
        self.donate = CTkButton(master=self.frame1, text="Donate", font=("Arial", 11, "bold"), fg_color="#031927", text_color="#C8E0F4", bg_color="#EBEBEB", width=10)
        self.donate.pack(side=LEFT, padx=5)
        
        #Button for forget the password
        self.buttonForgot = CTkButton(master=self.frame1, text="Forgot the password?", font=("Arial", 11, "bold"), fg_color="transparent", text_color="#547792", bg_color="#EBEBEB")
        self.buttonForgot.pack(side=LEFT)
        
        #Create an Account Button
        self.buttonCreateAcc = CTkButton(self.mainWindow, text="Create an Account", font=("Arial", 20),text_color="#C8E0F4", height=6, fg_color="#031927",hover_color="#189000", corner_radius=0)
        self.buttonCreateAcc.pack(fill=X, pady=1)
        
    def run(self):
        self.mainWindow.mainloop()
        
    def getEntryUser(self):
        return self.entryUser.get()
