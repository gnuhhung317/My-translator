from translator import Translator
from tkinter import *
from tkinter import messagebox

class RemoveWordWindow:
    def __init__(self):
        self.translator = Translator()
        self.window = Tk()
        self.window.iconbitmap("trans.ico")
        self.window.attributes('-topmost',True)
        self.window.title("Remove word")
        self.window.geometry("600x600")
        self.listbox = Listbox(self.window,width=30,font=("Arial",20))
        self.creat_listbox()
        Button(self.window,text="Remove",command=self.remove_word).pack()
        self.window.mainloop()
    def to_string(self,word):
        return f"{word[0]}: {word[1]}.   {word[2]}"

    def on_selection(self):
        selection = self.listbox.get(self.listbox.curselection())
        return selection
    def remove_word(self):
        try:
            self.translator.dictionary.pop(self.listbox.curselection()[0])
        except IndexError:
            message = messagebox.showerror(title="Error",message="Please choose an item!!")
        self.translator.save_dictionary()
        message = messagebox.showinfo("Remove successly",message="Remove successly!")
        self.window.destroy()
    
    def creat_listbox(self):
        for word in self.translator.dictionary:
            self.listbox.insert(END,self.to_string(word))
        self.listbox.pack()


