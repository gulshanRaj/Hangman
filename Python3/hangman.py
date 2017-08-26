import random

def game(word, meaning, noOfChances):
    found = [False]*len(word)
    lettersNotFound = len(word)
    displayWord = "_ " * len(word)
    for i in range(1, noOfChances+1):
        print("___________________________________________________")
        print("The given word means %s" %meaning)
        print("Remaining chances = %d " %(6-i))
        print(displayWord)
        wordIn = input("Guess the word or enter a character > ")
        if len(wordIn)>1:
            if(wordIn == word):
                foundCorrectWord(word)
                return
            else:
                print("This is not what I am looking for :-(")
        else:
            for j in range(0,len(word)):
                if(word[j] == wordIn):
                    displayWord = displayWord[:j*2]+wordIn+" "+displayWord[j*2+2:]
                    if not found[j]:
                        found[j] = True
                        lettersNotFound = lettersNotFound - 1
        if lettersNotFound <= 0:
            foundCorrectWord(word)
            return

    if lettersNotFound != 0:
        wordNotFound(word)

def foundCorrectWord(word):
    print("Correct")

def wordNotFound(word):
    print("The answer was %s" %word)

def selectWord():
    meanings = {"engrossed" : "engaged",
     "poignant": "painful to the feelings"}
    keys = list(meanings)
    choice = int(random.randrange(len(keys)))
    word = keys[choice]
    game(word, meanings[word] , len(word)//2)

def startGame():
    while True:
        userInput = input("[P]lay game\n[Q]uit\n")
        if userInput == 'P' or userInput == 'p':
            selectWord()
        elif userInput == 'Q' or userInput == 'q':
            return

startGame()
