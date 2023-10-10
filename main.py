import socket
import threading
import PIL
from tkinter import *
from PIL import ImageTk, Image

ws = Tk()

w_shift = ws.winfo_screenwidth() / 3 - 120
h_shift = 50

ws.title('Нажмите на кнопку!')
ws.geometry('700x700+%d+%d' % (w_shift, h_shift))
ws.resizable (False, False)

images = ["C:/Users/Admin/Desktop/pics/1.png",
          "C:/Users/Admin/Desktop/pics/2.jpeg",
          "C:/Users/Admin/Desktop/pics/3.png",
          "C:/Users/Admin/Desktop/pics/4.jpeg",
          "C:/Users/Admin/Desktop/pics/5.jpeg",
          "C:/Users/Admin/Desktop/pics/6.jpeg"]
im = Image.open(images[0])
ph = ImageTk.PhotoImage(im)

label = Label(ws, width = 700, height = 700, image=ph)
label.image = ph
label.pack()

def update(h):
    global im, ph
    ph = ImageTk.PhotoImage(Image.open(images[h % len(images)]))
    label.configure(image=ph)
    # label.pack()


def func():
    t = threading.Thread(target=sock)
    t.start()


def sock():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 9999))
    s.listen(1)
    #print("ждём")

    while 1:
        conn, addr = s.accept()
        #print(f"соединение установлено: {addr}")
        while 1:
            data = conn.recv(1024)
            if not data: break
            h = int.from_bytes(data, byteorder='big')
            #print(f"получены данные: {data}")
            update(h)
            conn.send(data)
        conn.close()

func()
ws.mainloop()
