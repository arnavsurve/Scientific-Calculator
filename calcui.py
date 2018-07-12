from tkinter import *

class calculator:
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.exitButton = Button(frame, text="OFF", command=self.exitProgram)
        self.exitButton.grid(row=0, column=0, sticky=W)

    def exitProgram(self):
        raise SystemExit


root = Tk()


b = calculator(root)


root.mainloop()
