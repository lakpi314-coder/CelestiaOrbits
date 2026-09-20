from tkinter import *
from tkinter import ttk
root = Tk()

root.geometry("200x200")
root.title("Celestia Keybindings")
frm = ttk.Frame(root, padding=10)
frm.grid()


ttk.Label(frm,text="Escape:E").grid(column=0,row=0)
ttk.Label(frm,text="Increase Velocity:I").grid(column=0,row=1)
ttk.Label(frm,text="Decrease Velocity:K").grid(column=0,row=2)
ttk.Label(frm,text="Increase Time:T").grid(column=0,row=3)
ttk.Label(frm,text="Decrease Time:G").grid(column=0,row=4)
ttk.Label(frm,text="Movement:WASD").grid(column=0,row=5)
ttk.Label(frm,text="Enter back:~").grid(column=0,row=6)





root.mainloop()