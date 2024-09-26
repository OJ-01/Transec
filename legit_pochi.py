"""
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('legit pochi')
root.geometry('900x500')
root.config()


var=tk.StringVar()
var.set('Account Balance')
bal = tk.Label(root, textvariable=var)
bal.pack()


class Window:
    def __init__ (self, master):
        self.master = master

        #frame
        self.frame = tk.Frame(self.master, width=1200, height=700)
        self.frame.pack()

        #label
        self.label = tk.Label(self.frame, text='User ID')
        self.label.place(x=50, y=20)

        self.entry0 = tk.Entry(self.frame)
        self.entry0.place(x=50,y=70)

        self.label = tk.Label(self.frame, text='Account Balance')
        self.label.place(x=50, y=120)

        self.entry = tk.Entry(self.frame)
        self.entry.place(x=50,y=170)

        self.label = tk.Label(self.frame, text='Transaction History')
        self.label.place(x=50, y=220)

        self.entry2 = tk.Entry(self.frame)
        self.entry2.place(x=50,y=270)


        #entry
        

       
root = tk.Tk()
root.title('Payment System')

window = Window(root)
root.mainloop()
"""
import tkinter as tk

class Window:
    def __init__(self, master):
        self.master = master

        # Frame
        self.frame = tk.Frame(self.master, width=300, height=300)
        self.frame.pack(pady=20)

        # User ID Label and Entry
        self.label_user_id = tk.Label(self.frame, text='User ID')
        self.label_user_id.place(x=10, y=20)

        self.entry_user_id = tk.Entry(self.frame)
        self.entry_user_id.place(x=150, y=20)

        # Account Balance Label and Entry
        self.label_balance = tk.Label(self.frame, text='Account Balance')
        self.label_balance.place(x=10, y=90)

        self.entry_balance = tk.Entry(self.frame)
        self.entry_balance.place(x=150, y=90)

        # Transaction History Label and Entry
        self.label_history = tk.Label(self.frame, text='Transaction History')
        self.label_history.place(x=10, y=160)

        self.entry_history = tk.Entry(self.frame)
        self.entry_history.place(x=10, y=190)

        # Define Buttons
        self.submit_button = tk.Button(self.frame, text='Send', command=self.submit)
        self.submit_button.place(x=10, y=130)

        self.clear_button = tk.Button(self.frame, text='Pay', command=self.clear)
        self.clear_button.place(x=100, y=130)

    def submit(self):
        # Logic for submit action
        user_id = self.entry_user_id.get()
        balance = self.entry_balance.get()
        history = self.entry_history.get()
        print(f"User ID: {user_id}, Balance: {balance}, History: {history}")

    def clear(self):
        # Logic for clearing the entries
        self.entry_user_id.delete(0, tk.END)
        self.entry_balance.delete(0, tk.END)
        self.entry_history.delete(0, tk.END)

# Main application
root = tk.Tk()
root.title('Payment System')
root.geometry('300x300')  # Adjust the window size

window = Window(root)
root.mainloop()
