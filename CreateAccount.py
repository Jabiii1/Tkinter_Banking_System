from customtkinter import *

accWindow = CTk()
accWindow.geometry("420x600")
accWindow.title("Create an Account")
accWindow.resizable(False, False)
set_appearance_mode("light")

title = CTkLabel(master=accWindow, text="Create your Account!",font=("Roboto", 24, "bold"))
title.pack(pady=10)


accWindow.mainloop()