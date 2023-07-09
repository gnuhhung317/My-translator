import json
class Translator:
    def __init__(self):
        self.dictionary = []
        self.load_dictionary()
    def load_dictionary(self):
        with open("dictionary.json",encoding="utf-8") as file:
            try:  
                self.dictionary = json.load(file)
            except json.decoder.JSONDecodeError:
                self.dictionary =[]
        
    def save_dictionary(self):
        self.dictionary = sorted(self.dictionary)
        with open("dictionary.json","w",encoding="utf-8") as file:
            json.dump(self.dictionary,file)
    def add_word(self,english,vietnamese,example):
        if english.strip() == "" or vietnamese.strip() =="":
            return "Failed"
        word = [english,vietnamese,example]
        self.dictionary.append(word)
        self.save_dictionary()
        self.load_dictionary()
    def show_all(self):
        self.load_dictionary()
        ans = ""
        i=1
        for word in self.dictionary:
            ans+=f"{i}. {word[0]}: {word[1]}. {word[2]}\n"
            
            i+=1
        return ans



