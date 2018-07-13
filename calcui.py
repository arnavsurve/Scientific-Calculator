from tkinter import *


class arnavButtons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.grid(row=0, column=0)

        self.firstNumberLabel = Label(frame, text="Enter first number: ")
        self.firstNumberLabel.grid(row=1, column=0, sticky=W)

        self.firstEntry = Entry(frame)
        self.firstEntry.grid(row=1, column=1)
        Entry.get(self)
        
        self.secondNumberLabel = Label(frame, text="Enter second number: ")
        self.secondNumberLabel.grid(row=2, column=0, sticky=W)

        self.secondEntry = Entry(frame)
        self.secondEntry.grid(row=2, column=1)
        


root = Tk()


b = arnavButtons(root)


root.mainloop()

