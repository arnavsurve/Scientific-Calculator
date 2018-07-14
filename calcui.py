from tkinter import *


class arnavButtons:

    def __init__(self, master):
        frame = Frame(master, bg="#021635")
        frame.pack(side=LEFT)

        # Quit Button
        self.quitButton = Button(frame, text="Quit", command=frame.quit, highlightbackground="red", fg="white")
        self.quitButton.grid(row=0, column=0, sticky=W, padx=7)

        # Labels for number entries and corresponding entries
        self.firstNumberLabel = Label(frame, text="Enter first number: ", bg="#021635", fg="white")
        self.firstNumberLabel.grid(row=1, column=0, sticky=E)

        self.firstEntry = Entry(frame, bg="#34435b", highlightbackground="#021635", fg="white")
        self.firstEntry.grid(row=1, column=1)
        
        def ugh():
            print(self.firstEntry.get())

        self.ughButton = Button(frame,text="ugh", command = ugh)
        self.ughButton.grid(row=5, column=1, sticky=S)

        self.secondNumberLabel = Label(frame, text="Enter second number: ", bg="#021635", fg="white")
        self.secondNumberLabel.grid(row=2, column=0, sticky=E)

        self.secondEntry = Entry(frame, bg="#34435b", highlightbackground="#021635", fg="white")
        self.secondEntry.grid(row=2, column=1)

        # Functions for the math functions (wtf)
        # def ugh():
        #     print(self.firstEntry.get())
        #
        # self.ughButton = Button(frame,text="ugh", command = ugh)
        # self.ughButton.grid(row=5, column=1, sticky=S)

        # def add():
        #     print(int(self.firstEntry.get()) + int(self.secondEntry.get())



        
        # Buttons for math functions
        self.addButton = Button(frame, text=" + ", highlightbackground="#021635", fg="white", command=add)
        self.addButton.grid(row=0, column=2, pady=3)

        def add():
            print(int(self.firstEntry.get()) + int(self.secondEntry.get())

        self.subtractButton = Button(frame, text=" - ", highlightbackground="#021635", fg="white")
        self.subtractButton.grid(row=1, column=2, pady=3)

        self.multiplyButton = Button(frame, text=" * ", highlightbackground="#021635", fg="white")
        self.multiplyButton.grid(row=2, column=2, pady=3)

        self.divideButton = Button(frame, text=" / ", highlightbackground="#021635", fg="white")
        self.divideButton.grid(row=3, column=2, pady=3)

        self.exponentButton = Button(frame, text=" ^ ", highlightbackground="#021635", fg="white")
        self.exponentButton.grid(row=4, column=2, pady=3)

        self.rootButton = Button(frame, text=" root ", highlightbackground="#021635", fg="white")
        self.rootButton.grid(row=5, column=2, pady=3, padx=3)

        self.factorialButton = Button(frame, text=" ! ", highlightbackground="#021635", fg="white")
        self.factorialButton.grid(row=6, column=2, pady=3)


root = Tk()


b = arnavButtons(root)


root.mainloop()

