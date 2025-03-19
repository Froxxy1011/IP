import requests
import time
import tkinter as tk
from tkinter import messagebox
class main:

    def getip():  
        global ip
        ip = requests.get('https://api.ipify.org').text
        messagebox.showinfo("IP Address", "Your IP Address is: " + ip)
        main.store()


    def tkinter_gui():
        gui = tk.Tk()
        
        title = gui.title("Ip_Address_Info")
        
        gui.geometry("150x100")
        
        gui.resizable(False,False)
        
        
        getpipi = tk.Button(gui, text="Get IP Address", command=main.getip, font=("Arial", 12), bg="blue", fg="white")
        getpipi.pack(pady=10)
        
        
        gui.mainloop()

    def store():
        with open('ip_log.txt', 'w') as file:
            file.write(ip)
        messagebox.showinfo("Stored","IP Address Stored Successfully")



main.tkinter_gui()

    