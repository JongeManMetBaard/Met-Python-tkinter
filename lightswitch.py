import tkinter as tk
window = tk.Tk()

button = tk.Button(text='', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code

def updateText(event):
    button.config(text='Switch light off')
    button.bind("<Button-1>", oldText)
    window.configure(bg='yellow')
    print("light is on")

def oldText(event):
    button.config(text='Switch light on')
    button.bind("<Button-1>", updateText)
    window.configure(bg='black')
    print("light is off") 

oldText("")


# schijf hier tussen je code

window.mainloop()