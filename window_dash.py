from tkinter import *

def inventory():
    window_inv = Toplevel(window)
    window_inv.title("Inventory")
    window_inv.geometry("1280x720")
    window_inv.configure(bg = "#ffffff")
    canvas = Canvas(
        window_inv,
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

    window_inv.resizable(False, False)
    window_inv.mainloop()
######################code for dashboard#######################################################################
def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#03a9f5")
canvas = Canvas(
    window,
    bg = "#03a9f5",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"backgrounddashboard.png")
background = canvas.create_image(
    641.0, 360.5,
    image=background_img)

img0 = PhotoImage(file = f"img0dashboard.png")
#dashboard button
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

img1 = PhotoImage(file = f"img1dashboard.png")

#inventory button
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = inventory,
    relief = "flat")

b1.place(
    x = 0, y = 179,
    width = 256,
    height = 46)

img2 = PhotoImage(file = f"img2dashboard.png")
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

img3 = PhotoImage(file = f"img3dashboard.png")
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

img4 = PhotoImage(file = f"img4dashboard.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 370, y = 200,
    width = 284,
    height = 152)
#inventory button
img5 = PhotoImage(file = f"img5dashboard.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = inventory,
    relief = "flat")

b5.place(
    x = 840, y = 200,
    width = 284,
    height = 152)

img6 = PhotoImage(file = f"img6dashboard.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b6.place(
    x = 840, y = 464,
    width = 284,
    height = 152)

img7 = PhotoImage(file = f"img7dashboard.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b7.place(
    x = 370, y = 464,
    width = 284,
    height = 152)

window.resizable(False, False)
window.mainloop()
