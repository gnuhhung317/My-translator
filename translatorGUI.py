from tkinter import *
from translator import *
from addwordwindow import AddWordWindow
from removewordwindow import RemoveWordWindow
from practicewindow import PraticeWindow
class TranslatorGUI:
    def __init__(self) :
        self.new_window = None
        
        self.translator = Translator()
        self.dictionary = self.translator.dictionary
        self.win = Tk()
        self.win.attributes('-topmost',True)
        self.win.iconbitmap("trans.ico")
        self.win.title("Translator for myself")
        self.english = ""
        self.vietnamese = ""
        self.example =""
        
        #UI
        Label(self.win,text="DucHung translator for reading",font=("Arial",30)).grid(row=0,column=0)

        self.main_frame = Frame(self.win)
        self.main_frame.grid(row=1,column=0)
        
        #show main frame
        Label(self.main_frame,text="English",font=("Arial",15)).grid(row=0,column=0,padx=10,pady=10)
        Label(self.main_frame,text="Tiếng Việt",font=("Arial",15)).grid(row=0,column=2)
        self.e_entry = Entry(self.main_frame,font = ("Arial",20),width=20)
        self.e_entry.grid(row=1,column=0,padx=10,pady=10)
        self.v_entry = Entry(self.main_frame,font = ("Arial",20),width=20)
        self.v_entry.grid(row=1, column=2,padx=10,pady=10)
        #translate button
        self.translate_button = Button(self.main_frame,text="Translate",command=self.translate,width=20,height=2)
        self.translate_button.grid(row=3,column=1,padx=10,pady=10)
        #add word button
        self.add_word_button = Button(self.main_frame,text="Add word",command=self.add_word,width=20,height=2)
        self.add_word_button.grid(row=4,column=1,padx=10,pady=10)
        #remove word button
        self.remove_word_button = Button(self.main_frame,text="Remove word",command=self.remove_word,width=20,height=2)
        self.remove_word_button.grid(row=5,column=1,padx=10,pady=10)
        #show all button
        self.show_all_button = Button(self.main_frame,text="Show all",command=self.show_all,width=20,height=2)
        self.show_all_button.grid(row=6,column=1,padx=10,pady=10)
        #practice button
        self.practice_button = Button(self.main_frame,text="Practice",command=self.practice,width=20,height=2)
        self.practice_button.grid(row=7,column=1,padx=10,pady=10)
        #textbox
        self.textbox = Text()
        self.textbox.grid(row=2,column=0,padx=10,pady=10)
        self.win.mainloop()
    def get_input_and_clear_ouput(self):
        self.english = self.e_entry.get().strip().lower()
        self.v_entry.delete(0,'end')
        self.textbox.delete("1.0",END)
    def translate(self):
        self.get_input_and_clear_ouput()
        check = 1
        if self.english.strip() == "":
            self.vietnamese = "Chưa nhập vào!"
            return
        for word in self.translator.dictionary:
            if word[0] == self.english:
                self.textbox.insert("1.0",word[2])
                self.vietnamese = word[1]
                check = 0
        if check:
            self.vietnamese = "chưa thêm vào"
        self.v_entry.insert(0,self.vietnamese)
        
            
    def add_word(self):
        add_word_window =AddWordWindow()
        self.translator.load_dictionary()
    def remove_word(self):
        remove_word_window = RemoveWordWindow()
        self.translator.load_dictionary()
    def show_all(self):
        self.textbox.delete("1.0",END)
        self.textbox.insert("1.0",self.translator.show_all())
    def practice(self):
        practice_window = PraticeWindow()



    
    
        
    
        
        
UI = TranslatorGUI()
    