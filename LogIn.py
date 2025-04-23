from customtkinter import *

mainWindow = CTk()
mainWindow.geometry("350x220")
mainWindow.title("CashG Bank System")
mainWindow.resizable(False, False)

set_appearance_mode("Light")
set_default_color_theme("dark-blue")

#LabelLogIn
labelLogin = CTkLabel(master=mainWindow, text="Log In your CashG Account", font=("Roboto", 24, "bold"), text_color="#031927")
labelLogin.pack(pady=10)

#Entry for username
entryUser = CTkEntry(master=mainWindow, width=200, height=24, placeholder_text="Username")
entryUser.pack(pady=5)

#Entry for password
entryPass = CTkEntry(master=mainWindow, width=200, height=24, placeholder_text="Password", show="*")
entryPass.pack(pady=10)

#Button for login
buttonLogIn = CTkButton(master=mainWindow, text="Log In", font=("Arial", 18, "normal"), text_color="#C8E0F4", fg_color="#031927", hover_color="#189000",width=200)
buttonLogIn.pack(pady=5)

#Frame for remember me and forget
frame1 = CTkFrame(mainWindow)
frame1.pack(padx=65,fill="both", expand=True)

#Checkbox for remember me
checkRememberMe = CTkCheckBox(master=frame1, text="Remember Me",font=("Arial", 11), checkbox_height=10, checkbox_width=10, bg_color="#EBEBEB", corner_radius=0)
checkRememberMe.pack(side=LEFT)

#Button for forget the password
buttonForgot = CTkButton(master=frame1, text="Forgot the password?", font=("Arial", 11), fg_color="transparent", text_color="#213448", height=25, bg_color="#EBEBEB", hover_color="#EBEBEB")
buttonForgot.pack(side=LEFT)

#Create an Account Button
buttonCreateAcc = CTkButton(mainWindow, text="Create an Account", font=("Arial", 20),text_color="#C8E0F4", height=6, fg_color="#031927",hover_color="#189000", corner_radius=0)
buttonCreateAcc.pack(fill=X, pady=1)

mainWindow.mainloop()
