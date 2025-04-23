from customtkinter import *

accWindow = CTk()
accWindow.geometry("420x400")
accWindow.title("Create an Account")
accWindow.resizable(False, False)
set_appearance_mode("light")

title = CTkLabel(master=accWindow, text="Create your Account!",font=("Roboto", 24, "bold"), text_color="#031927")
title.pack(pady=10)

Fname = CTkEntry

accWindow.mainloop()