# import PIL
# from PIL import Image,ImageTk
# import pytesseract
# import cv2
# from tkinter import *
# width, height = 800, 600
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# root = Tk()
# root.bind('<Escape>', lambda e: root.quit())
# lmain = Label(root)
# lmain.pack()

# def show_frame():
#     _, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
#     img = PIL.Image.fromarray(cv2image)
#     imgtk = ImageTk.PhotoImage(image=img)
#     lmain.imgtk = imgtk
#     lmain.configure(image=imgtk)
#     lmain.after(10, show_frame)

# show_frame()
# root.mainloop()
import subprocess
subprocess.call("./temp.sh",shell=True)
import tkinter
from tkinter import *

top = Tk()

def addNewlabel():
    L1 = Label(top, text="User Name")
    L1.pack( side = LEFT)
    E1 = Entry(top, bd =5)
    E1.pack(side = RIGHT)
    C = Button(top, text ="Add Sign", command = addNewSign)
    C.pack()



def addNewSign():
    print(E1.get())



B = Button(top, text ="Train", command = addNewlabel)


B.pack()

top.mainloop()