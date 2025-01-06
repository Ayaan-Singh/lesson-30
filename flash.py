class card:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__ (self):
        return self.word + '('+self.meaning+')'
flash = []   
print ("welcome to flashcard app 30mb to download")
while (True):
    word = str(input("enter a word "))
    meaning = str(input("enter the meaning  "))
    flash.append(card(word,meaning))
    opt = int(input(("enter 0 to make another flashcard and 1 to stop ")))
    if (opt):
        break

print ("\n your flashcards")
for i in flash :
    print (">",i)
