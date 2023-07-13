from tkinter import *
from translator import *
from tkinter import messagebox
from random import sample


class PraticeWindow:
    def __init__(self):
        self.words_quantity = 0
        self.words = []
        self.answer = []
        self.true_answer = []
        self.indice = 0
        self.translator = Translator()
        
        self.window = Tk()
        self.window.attributes("-topmost",True)
        self.window.title("Practice")
        self.window.iconbitmap("trans.ico")
        self.window.geometry("550x350")
        self.backward_button = Button()
        self.forward_button = Button()
        self.submit_button = Button()
        self.index_label = Label()
        self.word_label=Label()
        self.word_entry = Entry()
        self.quantity_frame = Frame()
        self.quantity_label = Label()
        self.quantity_entry = Entry()
        self.quantity_button = Button()
        self.ask_quantity()
        

        self.window.mainloop()

    def practice(self):
        #create widget to practice 

        Label(text="PRACTICE",font=("Arial",24)).grid(row=0,column=1,padx=20,pady=20)
        self.word_label = Label(self.window,text=f"{self.words[self.indice][0]}",font=("Arial",18))
        self.word_label.grid(row=1,column=1,padx=10,pady=10)
        self.word_entry = Entry(self.window,font=("Arial",20))
        self.word_entry.grid(row=2,column=1,padx=10,pady=10)
        self.word_entry.focus()
        
        self.backward_button = Button(self.window,text="<<",command=self.backward)
        self.backward_button.grid(row=3,column=0,padx=20,pady=20)
        self.forward_button = Button(self.window,text=">>",command=self.forward)
        self.forward_button.grid(row=3,column=2,padx=20,pady=20)
        self.submit_button = Button(self.window,text="Submit",font=("Arial",18),command=self.submit)
        self.submit_button.grid(row=3,column=1,padx=20,pady=20)

        self.index_label = Label(self.window,relief=SUNKEN,text=f"{self.indice+1} of {self.words_quantity}")
        self.index_label.grid(row=4,column=1,padx=10,pady=10)
    def reload(self):
        #reload the word lable and the index when click backward and forward button
        self.word_entry.delete(0,END)
        self.word_label.grid_forget()
        self.index_label.grid_forget()
        self.word_label = Label(self.window,text=f"{self.words[self.indice][0]}",font=("Arial",18))
        self.word_label.grid(row=1,column=1,padx=10,pady=10)
        self.index_label = Label(self.window,relief=SUNKEN,text=f"{self.indice+1} of {self.words_quantity}")
        self.index_label.grid(row=4,column=1,padx=10,pady=10)
    def backward(self):
        
        if self.indice ==0:
            self.indice = self.words_quantity-1
        else:
            self.indice -=1
        self.save_answer()
        self.reload()
        
    def forward(self):
        if self.indice == self.words_quantity-1:
            self.indice = 0
        else:
            self.indice +=1
        self.save_answer()
        self.reload()
    def submit(self):
        self.save_answer()
        self.word_entry.grid_forget()
        self.word_label.destroy()
        self.index_label.destroy()
        self.backward_button.destroy()
        self.forward_button.destroy()
        self.submit_button.destroy()
        
        self.make_key_table()

    def ask_quantity(self):
        # Ask how many world will be used for practice
        self.quantity_frame = Frame(self.window)
        self.quantity_frame.pack()
        self.quantity_label = Label(
            self.quantity_frame, text="Enter the words's number: ", font=("Arial", 14))
        self.quantity_label.grid(row=0, column=0, padx=10, pady=10)
        self.quantity_entry = Entry(self.quantity_frame, font=("Arial", 14))
        self.quantity_entry.grid(row=0, column=1, padx=10, pady=10)
        self.quantity_button = Button(
            self.window, text="Confirm", command=self.confirm)
        self.quantity_button.pack()
        self.quantity_entry.focus()

    def confirm(self):
        # Get the number,creat answer list, choose words and clear the screen
        if (self.quantity_entry.get().isdigit()):
            if int(self.quantity_entry.get())<=len(self.translator.dictionary):
                self.words_quantity = int(self.quantity_entry.get())
                self.choose_words()
                self.answer = ["None"]*self.words_quantity
                for i in range(self.words_quantity):
                    self.true_answer.append(IntVar())
                self.quantity_frame.destroy()
                self.quantity_button.destroy()
                self.practice()
            else:
                messagebox.showerror(message="Out of dictionary's quantiy!",title="error")
                
        else:
            messagebox.showerror(title="Invalid input",message="Invalid!")
        

    def save_answer(self):
        #save the answer
        answer = self.word_entry.get().strip()
        if answer=="":
            answer = "None"
        self.answer[self.indice] = answer
    def choose_words(self):
        # choose the words's quantity
        self.words = sample(self.translator.dictionary, k=self.words_quantity)
    def make_key_table(self):
        Label(self.window,text="Word").grid(row=1,column=0)
        Label(self.window,text="Meaning").grid(row=1,column=1)
        Label(self.window,text="Your answer").grid(row=1,column=2)
        Label(self.window,text="Correct").grid(row=1,column=3)
        for row,word in enumerate(self.words):
            Label(self.window,text=f"{word[0]}").grid(row=row+2,column=0)
            Label(self.window,text=f"{word[1]}").grid(row=row+2,column=1)
        for row,word in enumerate(self.answer):
            Label(self.window,text=f"{word}").grid(row=row+2,column=2)
            Checkbutton(self.window,text="True",variable=self.true_answer[row]).grid(row=row+2,column=3)
        for i in range(len(self.words)):
            self.window.grid_columnconfigure(i,weight=1)
            self.window.grid_rowconfigure(i,weight=1)
        Button(self.window,text="Calculate point",command=self.calculater_point).grid(row=self.words_quantity+2,column=1,columnspan=2)
    def calculater_point(self):
        point = 0
        for i in self.true_answer:
            if(i.get() == 1) :
                point+=1
        message1 = f"You are {point}/{self.words_quantity} point. "
        if (point>self.words_quantity*3/4):
            message1+="Good done!"
            messagebox.showinfo(title="Point",message=message1)
        elif point<self.words_quantity/2:
            message1+="You should learn more!"
            messagebox.showerror(title="Point",message=message1)
            
        
        self.window.destroy()
