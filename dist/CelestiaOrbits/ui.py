from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
root.title("CelestiaOrbits")
def Start():
    import subprocess 
    subprocess.run(["python", "main.py"])
def Keybind():
    import subprocess 
    subprocess.run(["python", "keybinds.py"])


ttk.Label(frm,text="Checkout keybindins before you Start! :)").grid(column=0,row=2)
ttk.Button(frm, text="start", command=Start).grid(column=1, row=0)
ttk.Button(frm, text="KeyBindings",command=Keybind).grid(column=1, row=3)
root.mainloop()
