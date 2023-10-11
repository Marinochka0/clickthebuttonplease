import socket
from tkinter import *
from tkinter import ttk


def aft():
    btn.config(text="Нажмите на кнопку",
               state="enabled")

def click_button():
    btn.config(text="Посмотрите на другой компьютер",
               state="disabled")
    btn.after(2000, aft)

    global clicks
    clicks += 1
    byteclicks = clicks.to_bytes(1, byteorder='big')
    s.send(byteclicks)


s = socket.socket()
s.connect(("192.168.134.23", 9999))

global clicks
clicks = 0

root = Tk()

w_shift = root.winfo_screenwidth() / 2 - 150
h_shift = root.winfo_screenheight() / 2 - 150

root.title("Кнопка")
root.geometry("300x100+%d+%d" % (w_shift, h_shift))
root.resizable(False, False)

btn = ttk.Button(root,
                 text="Нажмите на кнопку",
                 padding=10,
                 command=click_button)
btn.place(anchor=CENTER,
          relx=0.5,
          rely=0.5)

root.mainloop()
data = s.recv(1024)
s.close()
