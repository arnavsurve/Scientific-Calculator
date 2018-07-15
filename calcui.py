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

        self.secondNumberLabel = Label(frame, text="Enter second number: ", bg="#021635", fg="white")
        self.secondNumberLabel.grid(row=2, column=0, sticky=E)

        self.secondEntry = Entry(frame, bg="#34435b", highlightbackground="#021635", fg="white")
        self.secondEntry.grid(row=2, column=1)

        self.outputLabel = Label(frame, text=(int(self.firstEntry.get()) + int(self.secondEntry.get())))
        self.outputLabel.grid(row=2, column=3)


        # Buttons for math functions along with the functions
        
        def add():
             print(int(self.firstEntry.get()) + int(self.secondEntry.get()))

        self.addButton = Button(frame, text=" + ", highlightbackground="#021635", fg="white", command=add)
        self.addButton.grid(row=0, column=2, pady=3, padx=3)
        
        def subtract():
             print(int(self.firstEntry.get()) - int(self.secondEntry.get()))
        
        self.subtractButton = Button(frame, text=" - ", highlightbackground="#021635", fg="white", command=subtract)
        self.subtractButton.grid(row=1, column=2, pady=3, padx=10)

        def multiply():
             print(int(self.firstEntry.get()) * int(self.secondEntry.get()))
        
        self.multiplyButton = Button(frame, text=" * ", highlightbackground="#021635", fg="white", command=multiply)
        self.multiplyButton.grid(row=2, column=2, pady=3, padx=10)

        def divide():
            print(int(self.firstEntry.get()) / int(self.secondEntry.get()))
             
        self.divideButton = Button(frame, text=" / ", highlightbackground="#021635", fg="white", command=divide)
        self.divideButton.grid(row=3, column=2, pady=3, padx=10)

        def exponent():
             print(int(self.firstEntry.get()) ** int(self.secondEntry.get()))
        
        self.exponentButton = Button(frame, text=" ^ ", highlightbackground="#021635", fg="white", command=exponent)
        self.exponentButton.grid(row=4, column=2, pady=3, padx=10)

        def root():
             print((int(self.firstEntry.get())) ** (1/(int(self.secondEntry.get()))))
        
        self.rootButton = Button(frame, text=" root ", highlightbackground="#021635", fg="white", command=root)
        self.rootButton.grid(row=5, column=2, pady=3, padx=3)

        def factorial():
             from math import factorial
             print(factorial(int(self.firstEntry.get())))
        
        self.factorialButton = Button(frame, text=" ! ", highlightbackground="#021635", fg="white", command=factorial)
        self.factorialButton.grid(row=6, column=2, pady=3, padx=10)


root = Tk()


b = arnavButtons(root)


root.mainloop()

