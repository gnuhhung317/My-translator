from translator import*

from tkinter import *
class AddWordWindow:
    def __init__(self):
        self.new_english = ""
        self.new_vietnamese = ""
        self.new_example =""
        self.translator = Translator()
        
        self.new_window = Tk()
        self.new_window.iconbitmap("trans.ico")
        self.new_window.title("Add new word")
        self.new_window.geometry("600x300")
        
        new_frame = Frame(self.new_window)
        new_frame.pack()
        Label(new_frame,text="English: ",font=("Arial",15)).grid(row=0,column=0,padx=10,pady=10)
        self.new_e_entry= Entry(new_frame,font=("Arial",15),width=20)
        self.new_e_entry.grid(row=0,column=1,padx=10,pady=10)
        Label(new_frame,text="Vietnamese: ",font=("Arial",15)).grid(row=1,column=0,padx=10,pady=10)
        self.new_v_entry= Entry(new_frame,font=("Arial",15),width=20)
        self.new_v_entry.grid(row=1,column=1,padx=10,pady=10)
        Label(new_frame,text="Example: ",font=("Arial",15)).grid(row=2,column=0,padx=10,pady=10)
        self.new_ex_entry = Entry(new_frame,font=("Aria;",15),width=20)
        self.new_ex_entry.grid(row=2,column=1,padx=10,pady=10)
        
        Button(self.new_window,text="Add word",command=self.get_add_word).pack()
        self.new_window.mainloop()
    def get_add_word(self):
        self.new_english = self.new_e_entry.get()
        self.new_vietnamese = self.new_v_entry.get()
        self.new_example = self.new_ex_entry.get()
        self.add_new_word()
    def add_new_word(self):
        self.translator.add_word(self.new_english,self.new_vietnamese,self.new_example)
        self.new_window.destroy()
