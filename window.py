from tkinter import *




def dashboard():
    
    root1=Tk()
    root1.geometry("1280x720")
    root1.configure(bg = "#edf1f5")    
    root1.title("dashboard")
    canvas = Canvas(
    root1,
    bg = "#edf1f5",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
    canvas.place(x = 0, y = 0)

def inventory():
    
    root1=Tk()
    root1.geometry("1280x720")
    root1.title("inventory")
    root1.configure(bg = "#edf1f5")    
    canvas = Canvas(
    root1,
    bg = "#edf1f5",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
    canvas.place(x = 0, y = 0)





def reports():
    
    root1=Tk()
    root1.geometry("1280x720")
    root1.title("reports")
    root1.configure(bg = "#edf1f5")    
    canvas = Canvas(
    root1,
    bg = "#edf1f5",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    





window = Tk()

window.geometry("1280x720")
window.configure(bg = "#edf1f5")
window.title("pharmacy management system")
canvas = Canvas(
    window,
    bg = "#edf1f5",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    640.0, 360.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b_dashboard= Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = dashboard,
    relief = "flat")

b_dashboard.place(
    x = 0, y = 133,
    width = 256,
    height = 46)

img1 = PhotoImage(file = f"img1.png")
b_inventory = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = inventory,
    relief = "flat")

b_inventory.place(
    x = 0, y = 179,
    width = 256,
    height = 46)

img2 = PhotoImage(file = f"img2.png")
b_reports = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = reports,
    relief = "flat")

b_reports.place(
    x = 0, y = 225,
    width = 256,
    height = 46)



window.resizable(False, False)
window.mainloop()
