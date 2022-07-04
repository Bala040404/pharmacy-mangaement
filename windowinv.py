from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"backgroundinv.png")
background = canvas.create_image(
    640.5, 360.0,
    image=background_img)

img0 = PhotoImage(file = f"img0inv.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 0, y = 133,
    width = 256,
    height = 46)

img1 = PhotoImage(file = f"img1inv.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 0, y = 179,
    width = 256,
    height = 46)

img2 = PhotoImage(file = f"img2inv.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 0, y = 225,
    width = 256,
    height = 46)

img3 = PhotoImage(file = f"img3inv.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 0, y = 271,
    width = 256,
    height = 46)

window.resizable(False, False)
window.mainloop()
