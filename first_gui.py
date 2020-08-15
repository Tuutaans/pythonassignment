from tkinter import *
import random
from tkinter import messagebox
root = Tk()
root.title("Number Guessing Game")
root.geometry('620x400')                           
root.resizable(0, 0)                               # fixed size window
root.iconbitmap("d:/python/gasd.ico")               #  for icon



class NumberGuessing:
    number = IntVar()                                 #IntVar() for storing values
    num = IntVar()        
    guessed_number = IntVar()
    
    global value 
    value = 0

    #  creating buttons and text
    def __init__(self):
        

        self.from_label = Label(root, text ='From', font=("Helvetica", 18), fg="navy")
        self.from_label.grid(row=0, column=0, sticky=W, padx=5, pady=10)
        self.from_entry= Entry(root, textvariable=self.number, font=("Helvetica", 18), fg='black')
        self.from_entry.grid(row=0, column=1, padx=4, pady=4)
    
        self.to = Label(root, text ='To', font=("Helvetica", 18), fg="navy")
        self.to.grid(row=0, column=2, sticky=W, padx=5, pady=10)
        self.to_entry= Entry(root, textvariable=self.num, font=("Helvetica", 18), fg='black')
        self.to_entry.grid(row=0, column=3, padx=4, pady =4)

        self.labeling = Label(root, text ='Guess any number . Enter a range of number', font=("Helvetica", 18), fg="limegreen")
        self.labeling.grid(row=1, columnspan=4, pady=10)
        self.entry = Entry(root, textvariable=self.guessed_number, font=("Helvetica", 18), fg="black")
        self.entry.grid(row=2, columnspan=4, pady=10)

        self.button = Button(root, text="Check", font=("Times", 18), fg="navy", bg='silver', command=self.check)
        self.button.grid(row=3, columnspan=4, pady=10)

        self.Results = Label(root, text="", font=("Times", 18), fg="magenta")
        self.Results.grid(row=4, columnspan=4, pady=10)
        
        self.Results1 = Label(root, text="U may want to clear the 0 & give input", font=("Times", 18), fg="magenta")
        self.Results1.grid(row=5, columnspan=4, pady=10)

        self.Results2 = Label(root, font=("Times", 18), fg="magenta")
        self.Results2.grid(row=6, columnspan=4, pady=10)



    def check(self):
        try:
            self.number.get()
            self.num.get()
            self.guessed_number.get() 
            self.value = random.randint(self.number.get(), self.num.get())
            if self.number.get() == 0 & self.num.get() & self.guessed_number.get() == 0:
                self.Results.configure(text = f"Enter in all the fields")
               
        
            
            elif self.guessed_number.get () == self.value:
                self.labeling.grid_forget()
                self.Results.configure(text= f"Congrats, You Nailed It")
                self.Results1.configure(text = "Thanks for Playing Number Guessing game")
                self.Results2.configure(text = "Press the close button to end the game")
                self.exit = Button(root, text="close", font=("Times", 18), fg="red", command=root.quit, bd = 5 , relief =GROOVE)         #FOR EXIT BUTTON
                self.exit.grid(row=7, columnspan=4, pady=2, padx=10, sticky = W + E)
            
            else:
                self.labeling.grid_forget()
                self.Results.configure(text = f"Shit maan! the number is {self.value}")
                self.Results1.configure(text = "Press check again to get correct value")
                self.Results2.configure(text= "Or u can enter other value")
  
        except TclError:
            messagebox.showerror(title="Invalid Input", message="You can only enter number .This is a number guessing game")

xD = NumberGuessing()
root.mainloop()